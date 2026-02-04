from google import genai
import PIL.Image    
import sys
import time
import json
import os
# Khởi tạo client (DeepSeek tương thích với thư viện OpenAI)
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

# worker.py

def process_image(image_path):
    # Giả lập thời gian xử lý AI
   
      image = PIL.Image.open(image_path)
      response = client.models.generate_content(
          model = "gemini-2.5-flash", 
          contents=["Describe the image in 100 texts by vietnamese.", image]
      )
      return response.text

if __name__ == "__main__":
    # Nhận đường dẫn từ đối số dòng lệnh (sys.argv[1])
    if len(sys.argv) > 1:
        path = sys.argv[1]
        output = process_image(path)
        # IN RA JSON ĐỂ FASTAPI ĐỌC
        print(json.dumps(output))