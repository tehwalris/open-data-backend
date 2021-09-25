def smooth(df, dim, window_size):
  df = df.copy()
  df[dim] = df[dim].rolling(window_size).mean()
  df[f'{dim}_high'] = df[dim].rolling(window_size).quantile(0.9)
  df[f'{dim}_low'] = df[dim].rolling(window_size).quantile(0.1)
  return df