import unittest
import os
from CountryWrapper import countryWrapper

class TestCountryWrapper(unittest.TestCase):
  """Tests unitaires de CountryWrapper.py"""
  def __setup(self):
    """setup des différentes variables souvent utilisés"""
    self.DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    self.COUNTRY_WRAPPER_FR = countryWrapper('fr', self.DIR_PATH)
    self.COUNTRY_WRAPPER_EN = countryWrapper('en', self.DIR_PATH)

  def test_init_create_dictionnary_french(self):
    """Test que la création de la classe CountryWrapper crée le dictionnaire de pays en francais"""
    self.__setup()
    self.assertEqual(len(self.COUNTRY_WRAPPER_FR.countries), 197)

  def test_init_create_dictionnary_english(self):
    """Test que la création de la classe CountryWrapper crée le dictionnaire de pays en anglais"""
    self.__setup()
    self.assertEqual(len(self.COUNTRY_WRAPPER_EN.countries), 244)
  
  def test_init_bad_language(self):
    """Test que la creation de la classe de dictionnaire lance une erreur si ce n'est pas une langue supportee"""
    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    with self.assertRaises(Exception) as exception:
      countryWrapper('bad_language', DIR_PATH)

  def test_create_bad_wire_remove_two_countries(self):
    """Test que la methode de création de mauvaise association enlève 2 pays dans le dictionnaire de pays"""
    self.__setup()
    before = len(self.COUNTRY_WRAPPER_FR.countries)
    self.COUNTRY_WRAPPER_FR.create_bad_wire()
    after = len(self.COUNTRY_WRAPPER_FR.countries)
    self.assertEqual(before - after, 2)
  
  def test_create_bad_wire_add_to_removed_countries(self):
    """Test que la methode de création de mauvaise association ajoute 2 pays dans le dictionnaire de pays elevés"""
    self.__setup()
    before = len(self.COUNTRY_WRAPPER_FR.removed_countries)
    self.COUNTRY_WRAPPER_FR.create_bad_wire()
    after = len(self.COUNTRY_WRAPPER_FR.removed_countries)
    self.assertEqual(after - before, 2)
  
  def test_create_bad_wire_is_not_bomb(self):
    """Test que le fil créé par la méthode create_bad_wire n'est pas une bombe"""
    self.__setup()
    bad_wire = self.COUNTRY_WRAPPER_FR.create_bad_wire()
    self.assertEqual(bad_wire.is_bomb, False)
  
  def test_create_bad_wire_country_capital_not_matching(self):
    """Test que la création d'un mauvais lien crée un fil avec le pays et la capital qui ne correspondent pas"""
    self.__setup()
    bad_wire = self.COUNTRY_WRAPPER_FR.create_bad_wire()
    removed_country = self.COUNTRY_WRAPPER_FR.removed_countries[bad_wire.country]
    self.assertNotEqual(bad_wire.capital, removed_country)
  
  def test_create_bomb_remove_one_country(self):
    """Test que la création d'une bombe enlève un pays du dictionnaire de pays"""
    self.__setup()
    before = len(self.COUNTRY_WRAPPER_FR.countries)
    self.COUNTRY_WRAPPER_FR.create_bomb()
    after = len(self.COUNTRY_WRAPPER_FR.countries)
    self.assertEqual(before - after, 1)

  def test_create_bomb_add_to_removed_countries(self):
    """Test que la création de bombes ajoute le lien du dictionnaire de pays enlevés"""
    self.__setup()
    before = len(self.COUNTRY_WRAPPER_FR.removed_countries)
    self.COUNTRY_WRAPPER_FR.create_bomb()
    after = len(self.COUNTRY_WRAPPER_FR.removed_countries)
    self.assertEqual(after - before, 1)

  def test_create_bomb_is_bomb(self):
    """Test que la bombe créée est réellement une bombe"""
    self.__setup()
    bomb = self.COUNTRY_WRAPPER_FR.create_bomb()
    self.assertEqual(bomb.is_bomb, True)
  
  def test_create_bomb_country_capital_matching(self):
    """Test que la création de bombe crée un lien de pays dont la capital et le pays correspondent"""
    self.__setup()
    bomb = self.COUNTRY_WRAPPER_FR.create_bomb()
    removed_country = self.COUNTRY_WRAPPER_FR.removed_countries[bomb.country]
    self.assertEqual(bomb.capital, removed_country)
  
  def test_recreate_country_list_add_removed_elements(self):
    """Test que la méthode qui recrée le dictionnaire de pays ajoute les éléments enlevés"""
    self.__setup()
    before = len(self.COUNTRY_WRAPPER_FR.countries)
    for _ in range(5):
      self.COUNTRY_WRAPPER_FR.create_bomb()
    self.COUNTRY_WRAPPER_FR.recreate_country_list()
    after = len(self.COUNTRY_WRAPPER_FR.countries)
    self.assertEqual(before, after)

  def test_recreate_country_list_empty_removed_countries(self):
    """Test que la méthode qui recrée le dictionnaire de pays enlève les éléments du dictionnaire de pays enlevés"""
    self.__setup()
    for _ in range(5):
      self.COUNTRY_WRAPPER_FR.create_bomb()
    self.COUNTRY_WRAPPER_FR.recreate_country_list()
    after = len(self.COUNTRY_WRAPPER_FR.removed_countries)
    self.assertEqual(after, 0)

if __name__ == '__main__':
  """Tests de CountryWrapper"""
  unittest.main()