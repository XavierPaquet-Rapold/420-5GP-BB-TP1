import unittest
from Wire import wire

class TestWire(unittest.TestCase):
    def test_to_string_not_cut(self):
        """Test que la méthode __str__ de wire retourne le bon string quand le cable n'est pas coupé"""
        test_wire = wire('France', 'Paris', True)
        self.assertEqual('France ~~~~~~~ Paris', str(test_wire))

    def test_to_string_cut(self):
        """Test que la méthode __str__ de wire retourne le bon string quand le cable est coupé"""
        test_wire = wire('France', 'Paris', True)
        test_wire.cut()
        self.assertEqual('France ~~/ /~~ Paris', str(test_wire))

if __name__ == '__main__':
  """Tests de Wire"""
  unittest.main()