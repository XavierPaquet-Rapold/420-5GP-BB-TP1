from typing import List
import random
import os
from Tools import tools
from Wire import wire
from CountryWrapper import countryWrapper


def __create_index_bad_associations(nb_wire: int, min_bomb: int, max_bomb: int) -> List:
  """Calcul le nombre de bombes et crée une liste contenant les indexes des mauvaises association"""
  nb_bomb = random.randint(min_bomb, max_bomb)
  # Sélection des indexes des mauvaise associations
  bad_associations = [i for i in range(nb_wire)]
  for _ in range(nb_bomb):
    bad_associations.remove(random.choice(bad_associations))
  return bad_associations

def __create_wires(bad_associations: List, nb_wire: int, country_wrapper: countryWrapper):
  """Crée les liaisons en fonction des mauvaises associations"""
  wires = []
  for i in range(nb_wire):
    if i in bad_associations:
      wires.append(country_wrapper.create_bad_wire())
      continue
    wires.append(country_wrapper.create_bomb())
  return wires


def main() -> int:
  """Logique d'affaire du jeu GeoBomber"""
  DIR_PATH = os.path.dirname(os.path.realpath(__file__))
  MIN_BOMB = 1
  MAX_BOMB = 4
  NB_WIRE = 5
  language = tools.ask_language()
  if language == 'q':
    return 0
  try:
    user_query_tool = tools(language, DIR_PATH)
  except:
    print("Erreur d'analyse du fichier de chaînes | Error parsing the strings file")
    return 1
  user_query_tool.ask_name()
  try:
    country_wrapper = countryWrapper(language, DIR_PATH)
  except:
    user_query_tool.error_country_parsing()
    return 1
  bad_associations = __create_index_bad_associations(NB_WIRE, MIN_BOMB, MAX_BOMB)
  wires = __create_wires(bad_associations, NB_WIRE, country_wrapper)

if __name__ == "__main__":
  try:
    main()
  except:
    print("Erreur fatale, veuillez réessayer | fatal error, try again")
