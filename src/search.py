import pandas as pd
import pickle
import zipfile
from tqdm import tqdm
import numpy as np

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