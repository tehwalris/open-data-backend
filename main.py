from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src import air_quality



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

questions = [
  {
    'id': 1,
    'text': "How much carbon monoxide is there at Stampfenbachstrasse?",
    'function': air_quality.make_specific_answer_function('Zch_Stampfenbachstrasse', 'CO'),
  },
  {
    'id': 2,
    'text': "How much ozone is there at Stampfenbachstrasse?",
    'function': air_quality.make_specific_answer_function('Zch_Stampfenbachstrasse', 'O3'),
  },
  {
    'id': 3,
    'text': "Is air pollution in Zurich getting worse?",
    'function': air_quality.answer_combined_over_time,
  },
  {
    'id': [4, 5],
    'text': [
      'How much pollution is there in Zurich?',
      'What contributes to air pollution?',
  ],
  'function': air_quality.answer_pollutant_table,
  }
]

_questions = questions
questions = []
for group in _questions:
  if isinstance(group['id'], list):
    assert isinstance(group['text'], list)
    assert len(group['id']) == len(group['text'])
    for i in range(len(group['id'])):
      questions.append({ **group, 'id': group['id'][i], 'text': group['text'][i] })
  else:
    questions.append(group)

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
