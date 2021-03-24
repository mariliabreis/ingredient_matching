from fastapi import FastAPI
from typing import Optional
from model import word2vec

app = FastAPI()

@app.get('/')
def index():
  return {'ok': True}

# implement code into pipeline
# save model into model.joblib for prediction
# build a method in fastapi to call my model

@app.get("/most_similar/{ingredient}")
def read_item(ingredient: str):
  ms = word2vec(ingredient)
  return {"most_similar": ms}
