import os
import random
import re
from Wire import wire


class countryWrapper:
  """Wrapper qui contient la façon de parser les fichiers et créer les files"""
  COUNTRY_FILE_ENGLISH = 'national_capitals.csv'
  COUNTRY_FILE_FRENCH = 'liste-197-etats-2020.csv'

  def __init__(self, language: str, dir_path: str) -> None:
    """Constructeur"""
    self.countries = None
    self.language = language
    self.removed_countries = {}
    file_content = self.__read_file(dir_path)
    self.__create_country_dictionnary(file_content)

  def __read_file(self, dir_path: str) -> str:
    """Lis le fichier contenant les pays et capitales"""
    file = self.COUNTRY_FILE_ENGLISH if self.language == "en" else self.COUNTRY_FILE_FRENCH
    with open(os.path.join(dir_path, file), 'r', encoding="Latin1") as country_file:
        file_content = country_file.readlines()
    #supprimer la première ligne en français, car ce sont les titres de chaque colonne
    del file_content[0]
    return file_content

  def __create_country_dictionnary(self, file_content: str) -> dict:
    """Crée le dictionnaire de pays et capitales"""
    self.countries = {}
    for country_line in file_content:
        fields = re.split(';|,', country_line)
        country = fields[0]
        capital = fields[-1]
        self.countries[country] = capital.rstrip('\n')
  
  def create_bad_wire(self) -> wire:
    """Crée une mauvaise liaison et la retourne"""
    country_capital = []
    for i in range(2):
      country = random.choice(list(self.countries.items()))
      self.removed_countries[country[0]] = country[1]
      country_capital.append(country)
    self.countries.pop(country[0])
    country = country_capital[0][0]
    bad_capital = country_capital[1][1]
    return wire(country, bad_capital, False)

  def create_bomb(self) -> wire:
    """Crée une bonne liaison et la retourne"""
    country = random.choice(list(self.countries.items()))
    self.removed_countries[country[0]] = country[1]
    self.countries.pop(country[0])
    return wire(country[0], country[1], True)

  def recreate_country_list(self) -> None:
    """Remet les pays ayant été enlevés dans le dictionnaire de pays"""
    self.countries.update(self.removed_countries)
    self.countries = {}
