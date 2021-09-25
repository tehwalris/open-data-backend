from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src import air_quality
from src import random_facts



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
    'text': "How much carbon monoxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('CO'),
  },
  {
    'id': 6,
    'text': "How much nitrogen monoxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('NO'),
  },
  {
    'id': 7,
    'text': "How much nitrogen dioxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('NO2'),
  },
  {
    'id': [8, 9],
    'text': [
      "How much particulate matter is there in Zurich?",
      "How much PM10 is there in Zurich?",
    ],
    'function': air_quality.make_answer_pollutant_over_time('PM10'),
  },
  {
    'id': 10,
    'text': "How much PM2.5 is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('PM2.5'),
  },
  {
    'id': 11,
    'text': "How much sulfur dioxide is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('SO2'),
  },
  {
    'id': 2,
    'text': "How much ozone is there in Zurich?",
    'function': air_quality.make_answer_pollutant_over_time('O3'),
  },

  {
    'id': [3, 12],
    'text': [
      "Is air pollution in Zurich getting worse?",
      "How did air pollution in Zurich change over time?",
    ],
    'function': air_quality.answer_combined_over_time,
  },
  {
    'id': [4, 5],
    'text': [
      'How much pollution is there in Zurich?',
      'What contributes to air pollution?',
    ],
    'function': air_quality.answer_pollutant_table,
  },
  {
    'id': 13,
    'text': "How does air pollution in Zurich change throughout the year?",
    'function': air_quality.answer_over_year,
  },
  {
    'id': 14,
    'text': "How does air pollution in Zurich change throughout the day?",
    'function': air_quality.answer_over_day,
  },

  {
    'id': [15, 16, 17],
    'text': [
      "How tall is the tallest building in Zurich?",
      "How many floors does the biggest building in Zurich have?",
      "Where is the tallest building in Zurich?",
    ],
    'function': random_facts.make_answer_fact('Anzahl Stockwerke des höchsten Gebäudes (Adresse', 'floors'),
  },
  {
    'id': [18, 19],
    'text': [
      "How big are the districts of Zurich?",
      "What's the area of Zurich?",
    ],
    'function': random_facts.make_answer_fact('Fläche in Quadratkilometer', 'km²'),
  },
]

_questions = questions
questions = []
for group in _questions:
  assert isinstance(group['id'], list) == isinstance(group['text'], list)
  if isinstance(group['id'], list):
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
