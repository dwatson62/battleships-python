def char_range(c1, c2):
  """Generates the characters from `c1` to `c2`, inclusive."""
  for c in xrange(ord(c1), ord(c2)+1):
    yield chr(c)