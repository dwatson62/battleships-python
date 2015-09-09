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

  def create_board(self):
    board = []
    for i in range(0, 10): board.append([])
    letters = self.char_range('A', 'J')
    for i in range(1, 11):
      for j in range(1, 11):
        square = letters[i - 1] + str(j)
        board[i - 1].append(square)
    return board

  def char_range(self, c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    array = []
    for c in xrange(ord(c1), ord(c2)+1):
      array.append(chr(c))
    return array

  def display_own_board(self, player):
    board = self.create_board()
    for row in board:
      for index in range(len(row)):
        row[index] = self.check_own_square_status(row[index], player)
    return board

  def check_own_square_status(self, square, player):
    for ship in player.ships:
      if square in ship['positions']:
        newsquare = player.received_shots.get(square)
        if newsquare != None: return newsquare
      if square in ship['positions']: return 'SHIP'
    return '~'

  def display_opponent_board(self, player):
    board = self.create_board()
    for row in board:
      for index in range(len(row)):
        row[index] = self.check_opponent_square_status(row[index], player)
    return board

  def check_opponent_square_status(self, square, player):
    for ship in player.ships:
      if square in ship['positions']:
        newsquare = player.received_shots.get(square)
        if newsquare != None: return newsquare
    return '~'
