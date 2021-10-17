import random
import os
import sys
from Tools import tools
from typing import List
#faire pip install playsound
from playsound import playsound
from CountryWrapper import countryWrapper


def get_round_result(round_lost: bool, round_won: bool, name: str, user_query_tool: tools) -> str:
  """Recevoir la phrase de résultat de la partie"""
  if round_lost:
    return user_query_tool.get_message('round_lost')
  elif round_won:
    return user_query_tool.get_message('round_won', '{name}', name)

def create_index_bad_associations(nb_wire: int, min_bomb: int, max_bomb: int) -> List:
  """Calcul le nombre de bombes et crée une liste contenant les indexes des mauvaises association"""
  nb_bomb = random.randint(min_bomb, max_bomb)
  # Sélection des indexes des mauvaise associations
  bad_associations = [i for i in range(nb_wire)]
  for _ in range(nb_bomb):
    bad_associations.remove(random.choice(bad_associations))
  return bad_associations

def create_wires(bad_associations: List, nb_wire: int, country_wrapper: countryWrapper) -> List:
  """Crée les liaisons en fonction des mauvaises associations"""
  wires = []
  for i in range(nb_wire):
    if i in bad_associations:
      wires.append(country_wrapper.create_bad_wire())
      continue
    wires.append(country_wrapper.create_bomb())
  return wires

def show_wires(wires: list) -> str :
  """Montre la liste de cables, coupés ou pas"""
  wire_message = ''
  for i, wire in enumerate(wires):
    wire_message += f'[{i + 1:2d}] {wire}\n'
  return wire_message

def cut_wire(wires: list, cut_wire_index: int, user_query_tool: tools) -> bool:
  """Coupe le cable s'il n'est pas déjà coupé, et retourne si le cable était un bombe ou pas"""
  wire = wires[cut_wire_index]
  if not wire.is_cut:
    wire.cut()
    return wire.is_bomb
  print(user_query_tool.get_message('wire_already_cut'))
  return False

def check_for_win(wires: list) -> bool:
  """Retourne si toutes les mauvaises associations on été coupées"""
  for wire in wires:
    if not wire.is_cut and not wire.is_bomb:
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
  print(user_query_tool.get_message('start_game', '{name}', name))
  try:
    country_wrapper = countryWrapper(language, DIR_PATH)
  except:
    print(user_query_tool.get_message('error_country_parsing'))
    return 1

  score = 0
  continue_game = True
  while continue_game:
    bad_associations = create_index_bad_associations(NB_WIRE, MIN_BOMB, MAX_BOMB)
    wires = create_wires(bad_associations, NB_WIRE, country_wrapper)
    round_lost = False
    round_won = False
    print(user_query_tool.get_message('new_game', '{name}', name))

    while not round_lost and not round_won:
      print(show_wires(wires))
      cut_wire_index = user_query_tool.ask_wire_choice()
      if cut_wire_index == 0:
        break
      cut_wire_index -= 1
      round_lost = cut_wire(wires, cut_wire_index, user_query_tool)
      round_won = check_for_win(wires)
      if round_lost:
        playsound(os.path.join(DIR_PATH, 'public/explosion_track.wav'), block=False)
        score = 0
      if round_won:
        score += 1
    round_result = get_round_result(round_lost, round_won, name, user_query_tool)
    if round_result:
      print(round_result)
    print(user_query_tool.get_message('score', '{score}', str(score)))
    country_wrapper.recreate_country_list()
    continue_game = user_query_tool.ask_replay()

if __name__ == "__main__":
  """Point d'entrée de geobomber"""
  try:
    main()
  except KeyboardInterrupt:
    print('\nLe jeu a été interrompu | the game was interrupted')
  except:
    print('\nErreur fatale, veuillez réessayer | fatal error, try again')
