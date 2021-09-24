def memoize(f):
  value = None
  has_value = False

  def memoized():
    if has_value:
      return value
    value = f()
    has_value = True
    return value

  return memoized