﻿# Smart_shopping_cart with voice interation
 Sử dụng 3 models là STT-> LLM+RAG -> TTSTTS
Cách chạy : 
+ Cài đặt 
   ```
   pip install -r requirements.txt
   ``` 
+ Vào file .env trong mục src/backend/ 
   ```
   GEMINI_API_KEY=your_gemini_api_key
   ```

+ chạy backend
   ```
   cd src/backend/
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
