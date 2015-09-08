class Ship(object):

  def __init__(self, name):
    self.name = name
    self.get_length()

  def get_length(self):
    if self.name == 'Sub': self.length = 1
    if self.name == 'Destroyer': self.length = 2
    if self.name == 'Cruiser': self.length = 3
    if self.name == 'Battleship': self.length = 4
    if self.name == 'Carrier': self.length = 5

  def get_squares(self, position, orientation='H'):
    if orientation == 'H': return self.get_horizontal_squares(position)
    squares = self.get_vertical_squares(position)
    self.check_out_of_bounds(squares)
    return squares

  def get_horizontal_squares(self, position):
    squares = [position]
    for i in range(1, self.length):
      square = list(position)
      if square[-1] == '9': square[-1] = '10'
      else:
        square[-1] = (chr(ord(square[-1]) + i))
      squares.append("".join(square))
    return squares

  def get_vertical_squares(self, position):
    squares = [position]
    for i in range(1, self.length):
      square = list(position)
      square[0] = (chr(ord(square[0]) + i))
      squares.append("".join(square))
    return squares

  def check_out_of_bounds(self, squares):
    for square in squares:
      square = list(square)
      if square[0] not in self.char_range('A', 'J'):
        raise Exception('Out of bounds')
      del square[0]
      if int("".join(square)) > 10: raise Exception('Out of bounds')

  def char_range(self, c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in xrange(ord(c1), ord(c2)+1):
      yield chr(c)