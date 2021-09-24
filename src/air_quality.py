import pandas as pd
import glob
from .response import response_from_df
from pathlib import Path

def get_all_air_quality_csv_paths():
  return glob.glob(str(Path(__file__).parent / '../data/air_quality/*.csv'))

def load_single_air_quality_csv(path):
  df = pd.read_csv(
    path,
    parse_dates=["Datum"],
    dtype={
        'Standort': 'category',
        'Parameter': 'category',
    },
  )
  df = df[(df['Status'] == 'bereinigt') | (df['Status'] == 'provisorisch')]
  df = df.drop(columns=['Intervall', 'Status'])
  df = df.rename(columns={
      'Datum': 'date',
      'Standort': 'location',
      'Parameter': 'pollutant',
      'Einheit': 'unit',
      'Wert': 'value',
  })
  df = df.set_index('date')
  return df

def load_air_quality(group_by):
  day_df = []
  for path in get_all_air_quality_csv_paths():
    temp = load_single_air_quality_csv(path)
    temp = temp.groupby([group_by(temp.index), 'location', 'pollutant']).mean()
    day_df.append(temp)
  return pd.concat(day_df)

def make_specific_answer_function(location, pollutant):
  def answer_function():
    df = load_air_quality(lambda index: pd.Grouper(freq='M'))
    df = df.loc[pd.IndexSlice[:, location, pollutant]]
    df = df.reset_index()
    df = df.rename(columns={ 'date': 'x', 'value': 'y' })
    return response_from_df(df)

  return answer_function

def generic_answer_function():
  df = load_air_quality(lambda index: pd.Grouper(freq='M'))
  df = df.reset_index()
  df = df.groupby(['date', 'pollutant']).mean()['value'].unstack('pollutant')
  df = df.sort_index()
  df = df / df.iloc[0]
  df = df.mean(axis=1)
  df = df.reset_index()
  df = df.rename(columns={ 'date': 'x', 0: 'y' })
  return response_from_df(df)