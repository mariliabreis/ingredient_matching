from fastapi import FastAPI
from typing import Optional
import ast
from ingredient_matching.model_processing import *
from ingredient_matching.w2v import word2vec

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

@app.get("/find_combination")
def output_func(input_ingredient: str, num_matches: Optional[int] = 15, adventure: Optional[bool] = False, adventure_criteria: Optional[int]=20):
    # item_id: int, q: Optional[str] = None

    input_ingredient = ast.literal_eval(input_ingredient)
    # Combines other functions into a workflow
    num_matches += 1
    # num_matches = 11

    if type(input_ingredient) != list:
        input_ingredient = [input_ingredient]
    id_input = []

    for ingredient in input_ingredient:
        id_input.append(get_id(ingredient))
    min_ingredients = 0
    if adventure:
        min_ingredients = be_adventurous(id_input,adventure_criteria)
    id_list = find_match(id_input,num_matches,min_ingredients)
    names = list_to_names(id_list)
    return {'Recommendations': names}