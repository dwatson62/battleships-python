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


if __name__ == '__main__':
  unittest.main()