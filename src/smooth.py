import numpy as np

def smooth(df, dim, window_size):
  def stuff(s, q):
    s = s.rolling(window_size, center=True).quantile(q)
    s[s.diff() == 0] = np.nan
    s = s.interpolate('cubic')
    return s

  df = df.copy()
  df[f'{dim}_high'] = stuff(df[dim], 0.9)
  df[f'{dim}_low'] = stuff(df[dim], 0.1)
  df[dim] = df[dim].rolling(window_size, center=True).mean()
  return df