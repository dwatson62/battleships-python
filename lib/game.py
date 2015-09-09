import re

class Game(object):

  def __init__(self):
    self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    self.board = self.create_board()

  def declare_winner(self, player1, player2):
    if self.check_all_ships_sunk(player1) == True:
      return 'Player 2 wins!'
    if self.check_all_ships_sunk(player2) == True:
      return 'Player 1 wins!'

  def check_all_ships_sunk(self, player):
    for ship in player.ships:
      if ship['hits'] != 0: return False
    return True

  def create_board(self):
    board = [[] for _ in xrange(10)]
    for i in range(1, 11):
      for j in range(1, 11): board[i - 1].append('~')
    return board

  def display_board(self, player, which='ME'):
    board = self.board
    if which == 'ME': board = self.show_ships(player, board)
    return self.show_shots(player, board)

  def show_shots(self, player, board):
    for square in player.received_shots.keys():
      x, y = self.convert(square)
      board[x][y] = self.check_square_status(square, player)
    return board

  def show_ships(self, player, board):
    for ship in player.ships:
      for square in ship['positions']:
        x, y = self.convert(square)
        board[x][y] = 'SHIP'
    return board

  def convert(self, square):
    square = re.split('(\d+)', square)
    return [self.letters.index(square[0]), (int(square[1]) - 1)]

  def check_square_status(self, square, player):
    return player.received_shots.get(square) or '~'
