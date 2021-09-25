def smooth(df, dim, window_size):
  df = df.copy()
  df[f'{dim}_high'] = df[dim].rolling(window_size, center=True).max()
  df[f'{dim}_low'] = df[dim].rolling(window_size, center=True).min()
  df[dim] = df[dim].rolling(window_size, center=True).mean()
  return df