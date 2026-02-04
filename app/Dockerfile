# Sử dụng Python bản nhẹ
FROM python:3.11-slim

# Thiết lập thư mục làm việc
WORKDIR /code

# Cài đặt các thư viện cần thiết trước để tận dụng Docker cache
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy toàn bộ code vào container
COPY ./app /code/app

# Chạy ứng dụng với Uvicorn
# --host 0.0.0.0 là bắt buộc để Docker có thể ánh xạ port ra ngoài
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]