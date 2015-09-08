import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('lib'))
sys.path.append(lib_path)
from player import *
from ship import *

class TestShip(unittest.TestCase):

  def test_ship_has_name_on_creation(self):
    self.ship = Ship('Sub')
    self.assertEqual(self.ship.name, 'Sub')

  def test_sub_gets_correct_length(self):
    self.ship = Ship('Sub')
    self.assertEqual(self.ship.length, 1)

  def test_destroyer_gets_correct_length(self):
    self.ship = Ship('Destroyer')
    self.assertEqual(self.ship.length, 2)

  def test_destroyer_covers_two_squares(self):
    self.ship = Ship('Destroyer')
    self.squares = self.ship.get_horizontal_squares('B6')
    self.assertEqual(self.squares, ['B6', 'B7'])

  def test_destroyer_covers_two_squares_at_edge_of_board(self):
    self.ship = Ship('Destroyer')
    self.squares = self.ship.get_horizontal_squares('B9')
    self.assertEqual(self.squares, ['B9', 'B10'])


if __name__ == '__main__':
  unittest.main()