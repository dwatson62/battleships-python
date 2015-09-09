class Game(object):

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
        board[i - 1].append(square)
    return board

  def display_own_board(self, player):
    board = self.create_board()
    for row in board:
      for index in range(len(row)):
        row[index] = self.check_own_square_status(row[index], player)
    return board

  def check_own_square_status(self, square, player):
    newsquare = player.received_shots.get(square)
    if newsquare != None: return newsquare
    if newsquare == None:
      for ship in player.ships:
        if square in ship['positions']: return 'SHIP'
    return '~'

  def display_opponent_board(self, player):
    board = self.create_board()
    for row in board:
      for index in range(len(row)):
        row[index] = self.check_opponent_square_status(row[index], player)
    return board

  def check_opponent_square_status(self, square, player):
    newsquare = player.received_shots.get(square)
    if newsquare != None: return newsquare
    return '~'
