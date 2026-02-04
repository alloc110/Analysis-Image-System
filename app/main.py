from fastapi import FastAPI, File, UploadFile, HTTPException
import subprocess
import os
import json
import shutil
import sys
from prometheus_fastapi_instrumentator import Instrumentator 
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

resource = Resource.create({"service.name": "house-predict-service"})

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)


otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)

# 4. Thêm Processor để gửi dữ liệu theo đợt (tăng hiệu năng)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)
app = FastAPI(title="AI Image Processor")

FastAPIInstrumentor.instrument_app(app)

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/run_worker/")
async def run_worker_pipeline(file: UploadFile = File(...)):
    # 1. Kiểm tra định dạng
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Vui lòng gửi file hình ảnh!")

    # 2. Lưu file tạm thời
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # 3. CHẠY WORKER: Gọi file worker.py bằng subprocess
        # ['python', 'worker.py', 'đường/dẫn/ảnh']
        result = subprocess.run(
            [sys.executable, "app/worker.py", file_path],
            capture_output=True, 
            text=True,
            encoding='utf-8' # Đảm bảo đọc được tiếng Việt
        )

        # 4. Kiểm tra xem worker có chạy lỗi không
        if result.returncode != 0:
            return {"error": "Worker gặp sự cố", "details 1 ": result.stderr}

        # 5. Phân tích kết quả từ chuỗi JSON mà worker in ra
        worker_output = json.loads(result.stdout)
        
        return {
            "message": "Xử lý hoàn tất",
            "worker_result": worker_output
        }

    except Exception as e:
        return {"error 1": str(e)}
    
    finally:
        # 6. Tùy chọn: Xóa file sau khi xử lý xong để sạch máy
        if os.path.exists(file_path):
            os.remove(file_path)

Instrumentator().instrument(app).expose(app)