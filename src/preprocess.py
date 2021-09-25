import pandas as pd
import pickle
import zipfile
from tqdm import tqdm
import numpy as np

from . import air_quality
from . import search
from .path import get_path_from_root

if __name__ == "__main__":
  # print('preprocessing air_quality')
  # get_path_from_root('data/air_quality/pre').mkdir(exist_ok=True)
  # df = air_quality._load_air_quality(lambda index: index.date)
  # pd.to_pickle(df, get_path_from_root('data/air_quality/pre/monthly.pickle'))
  # df = air_quality._load_air_quality(lambda index: index.day_of_year)
  # pd.to_pickle(df, get_path_from_root('data/air_quality/pre/day_of_year.pickle'))
  # df = air_quality._load_air_quality(lambda index: index.hour)
  # pd.to_pickle(df, get_path_from_root('data/air_quality/pre/hour.pickle'))

  print('preprocessing embeddings')
  get_path_from_root('data/search/pre').mkdir(exist_ok=True)
  embedding_dict = search.create_embeddings_dict()
  with get_path_from_root('data/search/pre/embedding_dict.pickle').open(mode='wb') as f:
    pickle.dump(embedding_dict, f)