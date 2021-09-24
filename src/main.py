from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import air_quality

app = FastAPI()

questions = [
  {
    'id': 1,
    'text': "How much carbon monoxide is there at Stampfenbachstrasse?",
    'function': air_quality.make_answer_function('Zch_Stampfenbachstrasse', 'CO'),
  },
  {
    'id': 2,
    'text': "How much ozone is there at Stampfenbachstrasse?",
    'function': air_quality.make_answer_function('Zch_Stampfenbachstrasse', 'O3'),
  },
]

@app.get("/questions")
async def get_questions():
  return questions

class GetAnswerRequest(BaseModel):
  id: int

@app.post("/answer")
async def get_answer(req: GetAnswerRequest):
  question = None
  for q in questions:
    if q['id'] == req.id:
      question = q
  if question is None:
    raise HTTPException(status_code=404, detail="question not found")
  return question['function']()