import joblib
import pandas as pd

def kmeans():

  kmeans = joblib.load('models/kmeans.joblib')
  return kmeans

def word2vec(ingredient):

  word2vec = joblib.load('models/word2vec.joblib')
  ms = word2vec.wv.most_similar(ingredient)
  return ms
