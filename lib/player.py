class Player(object):

  def __init__(self):
    self.ships = []
    self.board = {}

  def place_ship(self, ship, position):
    self.ships.append( {'ship': ship.name, 'positions': ship.get_horizontal_squares(position) } )

  def shoot(self, player, position):
    for ship in player.ships:
      if position in ship['positions']:
        index = ship['positions'].index(position)
        ship['positions'][index] = 'HIT'
        player.board[position] = 'HIT'
        return self.check_has_sunk(ship)
    player.board[position] = 'X'
    return player.board[position]

  def check_has_sunk(self, ship):
    for square in ship['positions']:
      if square != 'HIT': return 'HIT'
    return 'SUNK'
