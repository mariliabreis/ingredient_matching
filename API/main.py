# from model import co_occurrence
import numpy as np
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

combination_percentage = pd.read_csv('../raw_data/baseline_front_end/combination_percentage.csv')
ordered_keys = pd.read_csv('../raw_data/baseline_front_end/ordered_keys.csv')

# define a root `/` endpoint
@app.get("/")
async def root():
    return {"ok": True}
# define endpoint for searching co-occurrences with one ingredient
@app.get("/co_occurrence/{search_word}")
def co_occurrence(search_word):
    word_index = ordered_keys[ordered_keys['replaced'] == search_word].index[0]
    ingredient_row = combination_percentage.iloc[word_index:word_index+1,:].T.sort_values(by=word_index, ascending=False)
    top_results = []
    for index in range(1,20):
        ingr_id = ingredient_row.T.columns[index]
        name = ordered_keys['replaced'].iloc[int(ingr_id)]
        top_results.append(name)
    return {'co_occurence': top_results}