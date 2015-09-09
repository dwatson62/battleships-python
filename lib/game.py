class Game(object):

  def __init__(self):
    self.board = self.create_board()
    self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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
    board = []
    for i in range(0, 10): board.append([])
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in range(1, 11):
      for j in range(1, 11):
        square = letters[i - 1] + str(j)
        board[i - 1].append('~')
    return board

  def display_board(self, player, which='ME'):
    board = self.board
    if which == 'ME':
      board = self.show_ships(player, board)
    board = self.show_shots(player, board)
    return board

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
    result = self.split_square(square)
    coords = [self.letters.index(result[0])]
    coords.append(int(result[1]) - 1)
    return coords

  def split_square(self, square):
    square = list(square)
    if len(square) == 3:
      square[1] = square[1] + square[2]
      square.pop()
    return square

  def check_square_status(self, square, player):
    return player.received_shots.get(square) or '~'
