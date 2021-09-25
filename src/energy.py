import pandas as pd
import numpy as np
import json

from .path import get_path_from_root
from .memoize import memoize
from .response import response_from_df
from .smooth import smooth

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

def power_weekly():
  df = load_data()
  df = df.groupby(pd.Grouper(freq="h")).sum()
  df = df[df>100].dropna()

  df["2020-06-18":"2020-06-30"] = df["2020-06-18":"2020-06-30"]/2

  df = df.groupby(pd.Grouper(freq="w")).mean()
  df = df.reset_index()
  df = df.rename(columns={ 'date': 'x', "energy": 'y' })
  return response_from_df(df)

def power_over_a_day():
  df = load_data()
  df = df.groupby(lambda x: x.hour).mean()
  df = df.reset_index()
  df = df.rename(columns={ 'index': 'x', "energy": 'y' })
  return response_from_df(df)

def power_over_a_week():
  df = load_data()
  df = df.groupby(lambda x: x.weekday()).mean()
  df = df.reset_index()
  df = df.rename(columns={ 'index': 'x', "energy": 'y' })
  return response_from_df(df)

def power_over_a_year():
  df = load_data()
  df = df.groupby(pd.Grouper(freq="h")).sum()
  df[df < 100] = np.nan

  df["2020-06-18":"2020-06-30"] = df["2020-06-18":"2020-06-30"]/2

  df = df.groupby(df.index.day_of_year).mean()

  df = df.reset_index()
  df = df.rename(columns={ 'date': 'x', "energy": 'y' })
  df = smooth(df, 'y', window_size=14)

  df = df.dropna()

  return response_from_df(df)