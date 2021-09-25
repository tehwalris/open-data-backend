import pandas as pd
import pickle
import zipfile
from tqdm import tqdm
import numpy as np
import re
from scipy import spatial

from .path import get_path_from_root
from .memoize import memoize

def create_embeddings_dict():
  embeddings_dict = {}
  with zipfile.ZipFile(str(get_path_from_root('data/search/glove.6B.csv')), 'r') as archive:
      with archive.open("glove.6B.50d.txt", 'r') as f:
          for line in tqdm(f, total=400000):
              line = str(line, encoding='utf-8')
              parts = line.strip().split(' ')
              word = parts[0]
              vec = np.asarray(parts[1:], "float32")
              embeddings_dict[word] = vec
  return embeddings_dict

def _load_embeddings_dict():
  with get_path_from_root('data/search/pre/embedding_dict.pickle').open(mode='rb') as f:
    return pickle.load(f)
    
load_embeddings_dict = memoize(_load_embeddings_dict)

stop_words = 'a the does did in zurich use how there'
stop_words = set(stop_words.split(' '))

def rough_tokenize(s):
    return [
        w.lower()
        for w in re.sub(r'[^a-zA-Z]', ' ', s.replace("'", '')).strip().split()
        if w.lower() not in stop_words
    ]

def rough_vecs_from_scentence(s, embeddings_dict):
    return [
        embeddings_dict[word]
        for word in rough_tokenize(s)
        if word in embeddings_dict
    ]

def make_rank_question(query, embeddings_dict):
  query_word_vecs = rough_vecs_from_scentence(query, embeddings_dict)
  
  def rank_question(question_word_vecs):
      distances_per_query_word = np.array([
          min(
              spatial.distance.euclidean(query_word_vec, question_word_vec)
              for question_word_vec in question_word_vecs
          )
          for query_word_vec in query_word_vecs
      ])
      rank = np.sum(distances_per_query_word ** 2)
      return np.nan_to_num(rank, np.inf)
  
  return rank_question