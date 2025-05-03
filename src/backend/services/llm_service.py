import google.generativeai as genai
import os
from dotenv import load_dotenv
from services.rag_service import RAGService

load_dotenv()

class LLMService:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.rag = RAGService()

    async def generate_answer(self, user_question: str) -> str:
        # Lấy thông tin từ RAG (Excel)
        rag_info = self.rag.search_item(user_question)

        # Prompt tổng hợp
        full_prompt = f"""
Bạn là trợ lý bán lẻ trong siêu thị.
Dưới đây là thông tin từ hệ thống nội bộ:
{rag_info}

Câu hỏi: {user_question}

Hãy trả lời ngắn gọn, chính xác và tự nhiên cho người dùng.
"""

        try:
            response = await self.model.generate_content_async(full_prompt)
            return response.text
        except Exception as e:
            return f"Lỗi LLM: {str(e)}"
