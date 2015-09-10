import re

def char_range(c1, c2):
  """Generates the characters from `c1` to `c2`, inclusive."""
  for c in xrange(ord(c1), ord(c2)+1):
    yield chr(c)

def check_out_of_bounds(square):
  square = re.split('(\d+)', square)
  if square[0] not in char_range('A', 'J'):
    out_of_bounds()
  if not 0 < int(square[1]) < 10:
    out_of_bounds()

def out_of_bounds():
  raise Exception('Out of bounds')
