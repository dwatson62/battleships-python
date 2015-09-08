class Player(object):

  def __init__(self):
    self.ships = []

  def place_ship(self, ship, position):
    self.ships.append( {'ship': ship.name, 'position': position} )