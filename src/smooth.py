import numpy as np

def smooth(df, dim, window_size):
  def stuff(s, q):
    s = q(s.rolling(window_size, center=True))
    s[s.diff() == 0] = np.nan
    s = s.interpolate('linear')
    return s

  df = df.copy()
  df[f'{dim}_high'] = stuff(df[dim], lambda v: v.max())
  df[f'{dim}_low'] = stuff(df[dim], lambda v: v.min())
  df[dim] = df[dim].rolling(window_size, center=True).mean()
  return df