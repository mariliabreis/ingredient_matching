from fastapi import FastAPI
from typing import Optional
from model import word2vec, most_popular, surprise
# other imports?

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

# gets most popular combinations with one ingredient
@app.get("/most_popular/{ingredient}")
def read_item(ingredient: str):
  mp = most_popular(ingredient)
  return {"most_popular": mp}

# gets surprising combinations with one ingredient, considering only the third top tier
@app.get("/surprise/{ingredient}")
def read_item(ingredient: str):
  sur = most_popular(ingredient)
  return {"surprise": sur}