import os
import unittest

from unittest.mock import patch
from Tools import tools
from Wire import wire
from CountryWrapper import countryWrapper
from GeoBomber import get_round_result
from GeoBomber import create_index_bad_associations
from GeoBomber import create_wires
from GeoBomber import show_wires
from GeoBomber import cut_wire
from GeoBomber import check_for_win

class GeoBomberTestCase(unittest.TestCase):
  """Tests unitaires de GeoBomber.py"""

  def test_get_round_result_round_won(self):
    """test que le message envoyé par get_round_result lors d'une partie gagnée est le bon"""
    tools_instance = tools('fr', os.path.dirname(os.path.realpath(__file__)))
    result_message = get_round_result(False, True, 'Hubert', tools_instance)
    self.assertEqual(result_message, 'OMG!!! Bombe désamorcée. Bravo Hubert!')

  def test_get_round_result_round_lost(self):
    """Test que le message envoyé par get_round_result lors d'une partie perdue est le bon"""
    tools_instance = tools('fr', os.path.dirname(os.path.realpath(__file__)))
    result_message = get_round_result(True, False, 'Hubert', tools_instance)
    self.assertEqual(result_message, '*** BOOM! ***')

  def test_create_index_bad_associations_max_bomb(self):
    """Test que la méthode de création d'indexe des mauvaises associations retourne moins de mauvaises associations que le maximum"""
    bad_associations_list = create_index_bad_associations(20, 5, 15)
    self.assertLessEqual(len(bad_associations_list), 15)

  def test_create_index_bad_associations_min_bomb(self):
    """Test que la méthode de création d'indexe des mauvaises associations retourne plus de mauvaises associations que le minimum"""
    bad_associations_list = create_index_bad_associations(20, 5, 15)
    self.assertGreaterEqual(len(bad_associations_list), 5)

  def test_create_index_bad_associations_no_same_bombs(self):
    """Test que la création des mauvaises associations contient seulement des éléments uniques"""
    bad_associations_list = create_index_bad_associations(100, 1, 2)
    contains_only_unique_elements = len(set(bad_associations_list)) == len(bad_associations_list)
    self.assertTrue(contains_only_unique_elements)

  def test_create_wires_create_bad_associations(self):
    """Vérifie que la création des fils crée des mauvaises associations"""
    bad_associations_list = [0, 1, 2, 3]
    wires = create_wires(bad_associations_list, 4, countryWrapper('fr', os.path.dirname(os.path.realpath(__file__))))
    has_bomb = False
    for wire in wires:
      if wire.is_bomb:
        has_bomb = True
    self.assertEqual(False, has_bomb)
  
  def test_create_wires_create_bombs(self):
    """Vérifie que la création des fils crée des bombes"""
    bad_associations_list = []
    wires = create_wires(bad_associations_list, 4, countryWrapper('fr', os.path.dirname(os.path.realpath(__file__))))
    has_bomb = False
    for wire in wires:
      if wire.is_bomb:
        has_bomb = True
    self.assertEqual(True, has_bomb)
  
  def test_create_wires_create_bombs_and_bad_associations(self):
    """Vérifie que la création des fils crée un mélange de bombes et de mauvaises associations"""
    bad_associations_list = [0, 2]
    wires = create_wires(bad_associations_list, 5, countryWrapper('fr', os.path.dirname(os.path.realpath(__file__))))
    nb_bomb = 0
    nb_bad_associations = 0
    for wire in wires:
      if wire.is_bomb:
        nb_bomb += 1
      else:
        nb_bad_associations += 1
    self.assertEqual(nb_bomb, 3)
    self.assertEqual(nb_bad_associations, 2)

  def test_show_wires_show_multiple_wires(self):
    """Vérifie que la méthode qui renvoie la représentation des fils fonctionne"""
    expected_output = '[ 1] country0 ~~~~~~~ capital0\n[ 2] country1 ~~~~~~~ capital1\n[ 3] country2 ~~/ /~~ capital2\n'
    wires = []
    wires.append(wire('country0', 'capital0', False))
    wires.append(wire('country1', 'capital1', True))
    wires.append(wire('country2', 'capital2', False))
    wires[2].cut()

    actual_output = show_wires(wires)

    self.assertEqual(expected_output, actual_output)

  def test_cut_wire_wire_not_cut(self):
    """Test que le fil se fait couper lorsque la méthode est appelée"""
    wires = []
    wires.append(wire('country0', 'capital0', False))
    wires.append(wire('country1', 'capital1', True))
    wires.append(wire('country2', 'capital2', False))
    is_bomb = cut_wire(wires, 0, None)
    self.assertFalse(is_bomb)

  @patch('builtins.print')
  def test_cut_wire_wire_cut(self, mock_print):
    """Test qu'un message d'erreur s'affiche si le fil était déjà coupé"""
    user_query = tools('fr', os.path.dirname(os.path.realpath(__file__)))
    wires = []
    wires.append(wire('country0', 'capital0', False))
    wires.append(wire('country1', 'capital1', True))
    wires.append(wire('country2', 'capital2', False))
    wires[0].cut()
    cut_wire(wires, 0, user_query)
    mock_print.assert_called_with('Aie! On se concentre svp...')

  def test_check_for_win_not_win_returns_false(self):
    """Test que la méthode check_for_win retourne false si tous les câbles à couper ne sont pas coupés"""
    wires = []
    wires.append(wire('country0', 'capital0', False))
    wires.append(wire('country1', 'capital1', True))
    wires.append(wire('country2', 'capital2', False))
    wires[0].cut()
    win_result = check_for_win(wires)
    self.assertFalse(win_result)
  
  def test_check_for_win_not_win_returns_false(self):
    """Test que la méthode check_for_win retourne false si tous les câbles à couper sont coupés"""
    wires = []
    wires.append(wire('country0', 'capital0', False))
    wires.append(wire('country1', 'capital1', True))
    wires.append(wire('country2', 'capital2', False))
    wires[0].cut()
    wires[2].cut()
    win_result = check_for_win(wires)
    self.assertTrue(win_result) 

if __name__ == '__main__':
  """Tests de CountryWrapper"""
  unittest.main()
