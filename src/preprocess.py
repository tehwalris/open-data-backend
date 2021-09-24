from . import air_quality
from .path import get_path_from_root
import pandas as pd

if __name__ == "__main__":
  print('preprocessing air_quality')
  get_path_from_root('data/air_quality/pre').mkdir(exist_ok=True)
  df = air_quality._load_air_quality(lambda index: index.date)
  pd.to_pickle(df, get_path_from_root('data/air_quality/pre/monthly.pickle'))
  df = air_quality._load_air_quality(lambda index: index.day_of_year)
  pd.to_pickle(df, get_path_from_root('data/air_quality/pre/day_of_year.pickle'))