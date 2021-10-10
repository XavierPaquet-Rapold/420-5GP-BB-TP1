import os
import random
from Wire import wire

class CountryWrapper:
  COUNTRY_FILE_ENGLISH = ""
  COUNTRY_FILE_FRENCH = "liste-197-etats-2020.csv"

  def __init__(self, language: str) -> None:
    self.countries = None
    self.language = language
    self.removed_countries = {}

  def __read_file(self) -> str:
    file = self.COUNTRY_FILE_ENGLISH if self.language == "en" else self.COUNTRY_FILE_FRENCH
    with open(os.path.join(os.getcwd(), self.file)) as country_file:
        file_content = country_file.readlines()
    if self.language == 'fr':
      #supprimer la première ligne, car ce sont les titres de chaque colonne
      del file_content[0]
    return file_content

  def __create_country_dictionnary(self) -> dict:
    file_content = self.__read_file()
    self.countries = {}
    for country_line in file_content:
        fields = country_line.split(';')
        country = fields[0]
        capital = fields[-1]
        self.countries[country] = capital.rstrip('\n')
  
  def create_bad_wire(self) -> wire:
    if self.countries == None:
      self.__create_country_dictionnary()
    country = random.choice(list(self.countries.keys()))
    self.removed_countries[country]
    del self.countries[country.]
    random_choice = random.choice(list(self.countries.values()))
    return wire()

  def create_bomb(self) -> wire:
    if self.countries == None:
      self.__create_country_dictionnary()
    return

  def recreate_country_list(self) -> None:
    self.countries.update(self.removed_countries)
    self.countries = {}
