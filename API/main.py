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
# get number of results according to how many there are (3% top?)
# or maybe usar can choose how many to return 
@app.get("/most_popular/{search_word}")
def most_popular(search_word):
    word_index = ordered_keys[ordered_keys['replaced'] == search_word].index[0]
    ingredient_row = combination_percentage.iloc[word_index:word_index+1,:].T.sort_values(by=word_index, ascending=False)
    top_results = []
    for index in range(1,20): # alter here to get percentage of results
        ingr_id = ingredient_row.T.columns[index]
        name = ordered_keys['replaced'].iloc[int(ingr_id)]
        top_results.append(name)
    return {'most_popular': top_results}

# define function that gets a random sample of ingredients, being on the first quartile? ou maybe the whole pool of results?
# the number of results should follow the same logic of the former endpoint
@app.get("/feeling_adventurous/{search_word}")
def feeling_adventurous(search_word):
    word_index = ordered_keys[ordered_keys['replaced'] == search_word].index[0]
    ingredient_row = combination_percentage.iloc[word_index:word_index+1,:].T.sort_values(by=word_index, ascending=False)
    top_results = []
    for index in range(1,20): # alter here to get percentage of results, create list of random indexes
        ingr_id = ingredient_row.T.columns[index]
        name = ordered_keys['replaced'].iloc[int(ingr_id)]
        top_results.append(name)
    return {'co_occurence': top_results}
