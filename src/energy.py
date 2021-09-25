import pandas as pd
import numpy as np
import json

from .path import get_path_from_root
from .memoize import memoize
from .response import json_from_df

def _load_data():
  df = pd.read_csv(
    get_path_from_root('data/energy/data.csv'),
    parse_dates=['zeitpunkt'],
    dtype={
      'status': 'category',
    },
  )
  df = df.rename(columns={
    'zeitpunkt': 'date',
    'bruttolastgang': 'energy',
  })
  df = df[(df['status'] == 'E') | ((df['status'] == 'F') & (df['energy'] >= 1000))]
  df = df.drop(columns=['status'])
  df = df.set_index('date')
  return df

load_data = memoize(_load_data)