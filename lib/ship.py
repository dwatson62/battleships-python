class Ship(object):

  def __init__(self, name):
    self.name = name
    self.length = self.get_length()
    self.hits = self.length

  def get_length(self):
    if self.name == 'Sub': return 1
    if self.name == 'Destroyer': return 2
    if self.name == 'Cruiser': return 3
    if self.name == 'Battleship': return 4
    if self.name == 'Carrier': return 5
    raise Exception('Ship not available')

  def get_squares(self, player, position, orientation='H'):
    if orientation == 'H': squares = self.get_horizontal_squares(position)
    else: squares = self.get_vertical_squares(position)
    self.check_out_of_bounds(squares)
    self.check_overlapping(player, squares)
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

  def check_overlapping(self, player, squares):
    for square in squares:
      for ship in player.ships:
        if square in ship['positions']:
          raise Exception('Cannot overlap ships')