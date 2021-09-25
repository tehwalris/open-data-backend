def memoize(f):
  value = None
  has_value = False

  def memoized():
    nonlocal value, has_value 
    if has_value:
      return value
    value = f()
    has_value = True
    return value

  return memoized