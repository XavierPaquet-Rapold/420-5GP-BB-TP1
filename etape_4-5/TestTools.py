import unittest
import sys
import os
from Tools import tools

class TestTools(unittest.TestCase):
  """Tests unitaires de la classe tools"""
  def test_init_creates_dictionnary(self):
    """Test que le constructeur de tools remplie un dictionnaire"""
    tool = tools('fr', os.path.dirname(os.path.realpath(__file__)))
    
    self.assertGreater(len(tool.strings), 3)

  def test_init_throw_error(self):
    """Test que le constructeur de tools retourne une exception si la langue indiquée est mauvaise"""
    with self.assertRaises(Exception) as exception:
      tool = tools('error', os.path.dirname(os.path.realpath(__file__)))

  def test_get_message_french(self):
    """Test que la méthode get_message retourne une string en français"""
    tool = tools('fr', os.path.dirname(os.path.realpath(__file__)))

    message = tool.get_message('ask_name')

    self.assertEqual('Bienvenue démineur. Quel est ton nom? ', message)
  
  def test_get_message_english(self):
    """Test que la méthode get_message retourne une string en anglais"""
    tool = tools('en', os.path.dirname(os.path.realpath(__file__)))

    message = tool.get_message('ask_name')

    self.assertEqual('Welcome deminer. What is your name? ', message)
  
  def test_get_message_replace_string(self):
    """Test que la méthode get_message retourne une string en remplaçant une partie du message"""
    tool = tools('fr', os.path.dirname(os.path.realpath(__file__)))

    message = tool.get_message('start_game', '{name}', 'Éric')

    self.assertEqual('Éric, quel nom ridicule pour un démineur! Enfin, allons-y même...', message)

if __name__ == '__main__':
  """Tests de Tools"""
  unittest.main()