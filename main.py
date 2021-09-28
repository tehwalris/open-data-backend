from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.questions import questions
from src.search import load_embeddings_dict, load_question_vecs, search_questions

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/questions")
async def get_questions():
  return questions

@app.get("/answer/{id}")
async def get_answer(id: int):
  question = None
  for q in questions:
    if q['id'] == id:
      question = q
  if question is None:
    raise HTTPException(status_code=404, detail="question not found")
  return question['function']()

@app.post("/search")
async def get_search_results(query: str):
  question_vecs = load_question_vecs()
  embeddings_dict = load_embeddings_dict()
  return search_questions(query, question_vecs, embeddings_dict)