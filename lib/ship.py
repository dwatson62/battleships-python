class Ship(object):

  def __init__(self, name):
    self.name = name
    self.get_length()

  def get_length(self):
    if self.name == 'Sub': self.length = 1
    if self.name == 'Destroyer': self.length = 2

  def get_squares(self, position, orientation='H'):
    if orientation == 'H': return self.get_horizontal_squares(position)
    return self.get_vertical_squares(position)

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