import pandas as pd
import numpy as np
import json

from .path import get_path_from_root
from .memoize import memoize
from .response import response_from_df

def _load_data():
  df = pd.read_csv(
    get_path_from_root('data/dogs/data.csv'),
    dtype={
      'status': 'category',
    },
  )
  return df

load_data = memoize(_load_data)


def dog_gender():
  df = load_data()
  df = df["GESCHLECHT_HUND"].value_counts()
  print("asdf")


  df = df.reset_index()
  df.columns =["label","value"]
  print(df)
  return response_from_df(df)
