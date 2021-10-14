import random
import os
import sys
from Tools import tools
from typing import List
from Wire import wire
#faire pip install playsound
from playsound import playsound
from CountryWrapper import countryWrapper

def __print_round_result(round_lost: bool, round_won: str, name: str, user_query_tool: tools):
  if round_lost:
    user_query_tool.print_round_lost()
  elif round_won:
    user_query_tool.print_round_won(name)

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

def __show_wires(wires: list) -> None:
  """Montre la liste de cables, coupés ou pas"""
  for i, wire in enumerate(wires):
    print(f"[{i + 1:2d}] {wire}")

def __cut_wires(wires: list, cut_wire_index: int, user_query_tool: tools) -> bool:
  """Coupe le cable s'il n'est pas déjà coupé, et retourne si le cable était un bombe ou pas"""
  wire = wires[cut_wire_index]
  if not wire.is_cutted:
    wire.cut_cable()
    return wire.is_bomb
  user_query_tool.print_wire_already_cut()
  return False

def __check_for_win(wires: list) -> bool:
  """Retourne si toutes les mauvaises associations on été coupées"""
  for wire in wires:
    if not wire.is_cutted and not wire.is_bomb:
      return False
  return True

def main() -> int:
  """Logique d'affaire du jeu GeoBomber"""
  sys.stdout.reconfigure(encoding='utf-8')
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
  name = user_query_tool.ask_name()
  user_query_tool.print_start_game(name)
  try:
    country_wrapper = countryWrapper(language, DIR_PATH)
  except:
    user_query_tool.error_country_parsing()
    return 1

  score = 0
  quit_game = False
  while not quit_game:
    bad_associations = __create_index_bad_associations(NB_WIRE, MIN_BOMB, MAX_BOMB)
    wires = __create_wires(bad_associations, NB_WIRE, country_wrapper)
    round_lost = False
    round_won = False
    while not round_lost and not round_won:
      user_query_tool.print_new_game(name)
      __show_wires(wires)
      cut_wire_index = user_query_tool.ask_wire_choice()
      if cut_wire_index is 0:
        break
      cut_wire_index -= 1
      round_lost = __cut_wires(wires, cut_wire_index, user_query_tool)
      round_won = __check_for_win(wires)
      if round_lost:
        playsound(os.path.join(DIR_PATH, 'explosion_track.wav'), block=False)
    __print_round_result(round_lost, round_won, name, user_query_tool)
    country_wrapper.recreate_country_list()
    quit_game = True if user_query_tool.ask_replay() == 'n' else False
  user_query_tool.print_score(score)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print('\nLe jeu a été interrompu | the game was interrupted')
  except:
    print('\nErreur fatale, veuillez réessayer | fatal error, try again')
