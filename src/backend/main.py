from fastapi import FastAPI
from pydantic import BaseModel
from services.llm_service import LLMService

app = FastAPI()
llm = LLMService()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(question_req: QuestionRequest):
    answer = await llm.generate_answer(question_req.question)
    return {"answer": answer}
