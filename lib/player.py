from game import Game

class Player(object):

  def __init__(self, name):
    self.ships = []
    self.fired_shots = {}
    self.received_shots = {}
    self.name = name

  def place_ship(self, ship, position, orientation='H'):
    self.ships.append( {'ship': ship.name, 'positions': ship.get_squares(self, position, orientation), 'hits': ship.hits } )

  def shoot(self, player, position):
    for ship in player.ships:
      if position in ship['positions']:
        ship['hits'] -= 1
        self.fired_shots[position] = 'HIT'
        player.received_shots[position] = 'HIT'
        return self.check_has_sunk(ship, player)
    player.fired_shots[position] = 'X'
    self.received_shots[position] = 'X'
    return 'X'

  def check_has_sunk(self, ship, player):
    if ship['hits'] > 0: return 'HIT'
    for square in ship['positions']:
      self.fired_shots[square] = 'SUNK'
      player.received_shots[square] = 'SUNK'
    return 'SUNK'
