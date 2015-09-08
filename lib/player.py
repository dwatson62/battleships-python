class Player(object):

  def __init__(self):
    self.ships = []
    self.fired_positions = []

  def place_ship(self, ship, position, orientation='H'):
    self.ships.append( {'ship': ship.name, 'positions': ship.get_squares(position, orientation) } )


  def shoot(self, player, position):
    self.fired_positions.append(position)
    for ship in player.ships:
      if position in ship['positions']:
        index = ship['positions'].index(position)
        ship['positions'][index] = 'HIT'
        return self.check_has_sunk(ship)
    return 'X'

  def check_has_sunk(self, ship):
    for square in ship['positions']:
      if square != 'HIT': return 'HIT'
    ship['positions'] = 'SUNK'
    return 'SUNK'
