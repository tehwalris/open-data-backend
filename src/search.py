import pandas as pd
import pickle
import zipfile
from tqdm import tqdm
import numpy as np
import re
from scipy import spatial

from .path import get_path_from_root
from .memoize import memoize
from .questions import questions

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

def _load_question_vecs():
  embeddings_dict = load_embeddings_dict()
  return [
      rough_vecs_from_sentence(q['text'], embeddings_dict)
      for q in questions
  ]

load_question_vecs = memoize(_load_question_vecs)

def stem_word(w, embeddings_dict):
  if w == 'does':
    return w
  stemmed = re.sub(r's$', '', w)
  if embeddings_dict is None or stemmed in embeddings_dict:
    return stemmed
  return w

stop_words = 'a the does did how much is in zurich use there what whats where'
stop_words = set(stem_word(w, None) for w in stop_words.split(' '))

def rough_tokenize(s, embeddings_dict):
    words = [
        stem_word(w.lower(), embeddings_dict)
        for w in re.sub(r'[^a-zA-Z]', ' ', s.replace("'", '')).strip().split()
    ]
    return [
      w
      for w in words
      if w not in stop_words
    ] 

def rough_vecs_from_sentence(s, embeddings_dict):
    return [
        embeddings_dict[word]
        for word in rough_tokenize(s, embeddings_dict)
        if word in embeddings_dict
    ]

bad_rank = (35, 0)
terrible_rank = (1e6, 0)

def make_rank_question(query, embeddings_dict):
  query_word_vecs = rough_vecs_from_sentence(query, embeddings_dict)
  
  def rank_question(question_word_vecs):
      if len(query_word_vecs) == 0 or len(question_word_vecs) == 0:
        return terrible_rank

      distances_per_query_word = np.array([
          min(
              spatial.distance.euclidean(query_word_vec, question_word_vec)
              for question_word_vec in question_word_vecs
          )
          for query_word_vec in query_word_vecs
      ])
      return (np.mean(distances_per_query_word ** 2), len(question_word_vecs))
  
  return rank_question

def search_questions(query, question_vecs, embeddings_dict):
  rank_question = make_rank_question(query, embeddings_dict)
  temp = [
      { 'id': q['id'], 'rank': rank_question(q_vec) }
      for q, q_vec in zip(questions, question_vecs)
  ]
  temp.sort(key=lambda e: e['rank'])
  return [
    r 
    for r in temp
    if r['rank'] < bad_rank
  ][:15]