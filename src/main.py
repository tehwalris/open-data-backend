from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

questions = [
  { 'id': 1, 'text': "How much carbon monoxide is there at Stampfenbachstrasse?" },
  { 'id': 2, 'text': "How much ozone is there at Stampfenbachstrasse?" },
]

@app.get("/questions")
async def get_questions():
  return questions