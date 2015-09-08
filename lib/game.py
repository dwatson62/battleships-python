class Game(object):

  def declare_winner(self, player1, player2):
    if self.check_ships(player1) == True:
      return 'Player 2 wins!'
    if self.check_ships(player2) == True:
      return 'Player 1 wins!'

  def check_ships(self, player):
    for ship in player.ships:
      if ship['hits'] != 0: return False
    return True

  def display_own_board(self, player):
    board = []
    for i in range(0, 10): board.append([])
    letters = self.char_range('A', 'J')
    for i in range(1, 11):
      for j in range(1, 11):
        square = letters[i - 1] + str(j)
        square = self.check_square_status(square, player)
        board[i - 1].append(square)
    return board

  def char_range(self, c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    array = []
    for c in xrange(ord(c1), ord(c2)+1):
      array.append(chr(c))
    return array

  def check_square_status(self, square, player):
    for ship in player.ships:
      for spot in ship['positions']:
        if spot == square:
          return player.received_shots.get(spot)
        if square in ship['positions']:
          return 'SHIP'
    return square
