from game import Game
from helpers import *
import re

class Player(object):

  def __init__(self, name):
    self.ships = []
    self.fired_shots = []
    self.received_shots = {}
    self.name = name

  def place_ship(self, ship, position, orientation='H'):
    self.ships.append( {'ship': ship.name, 'positions': ship.get_squares(self, position, orientation), 'hits': ship.hits } )

  def shoot(self, player, position):
    check_out_of_bounds(position)
    self.check_has_already_fired(position)
    for ship in player.ships:
      if position in ship['positions']:
        self.has_hit(ship, player, position)
        return self.check_has_sunk(ship, player)
    return self.has_missed(player, position)

  def check_has_already_fired(self, position):
    if position in self.fired_shots:
      raise Exception('Already fired once')

  def has_hit(self, ship, player, position):
    ship['hits'] -= 1
    self.fired_shots.append(position)
    player.received_shots[position] = 'HIT'

  def has_missed(self, player, position):
    self.fired_shots.append(position)
    player.received_shots[position] = 'X'
    return 'X'

  def check_has_sunk(self, ship, player):
    if ship['hits'] > 0: return 'HIT'
    for square in ship['positions']:
      player.received_shots[square] = 'SUNK'
    return 'SUNK'
