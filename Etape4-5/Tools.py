import json
import os


class tools:
  """Classe contenant les affichages"""
  def __init__(self, language: str, dir_path: str) -> None:
    if language != 'fr' and language != 'en':
      raise Exception('Language not supported')
    self.language = language
    with open(os.path.join(dir_path, 'strings.json'), 'r') as strings_file:
      self.strings = json.load(strings_file)
    
  def ask_name(self) -> str:
    """Affichage de la demande du nom"""
    while True:
      name = input(self.strings['ask_name'][self.language])
      if name.isalpha():
        return name
      else:
        print(self.strings['error_name'][self.language])
  
  def error_country_parsing(self) -> None:
    print(self.strings['error_country_parsing'][self.language])

  @staticmethod
  def ask_language() -> str:
    """Demander la langue du jeu"""
    while True:
      language = input("Veuillez indiquer la langue de votre choix ou quitter avec 'q'\n" +
        "Please indicate the language of your choice (en, fr) or quit with 'q': ").lower()
      if language == 'fr' or language == 'en' or language == 'q':
        return language
      else:
        print("Merci d'entrer 'fr' ou 'en' | Please enter 'en' or 'fr'")

  def ask_wire_choice(self) -> int:
    """Demander l'index du cable qui va etre coupé"""
    while True:
      wire_input = input(self.strings['ask_wire_choice'][self.language]).lower()
      if wire_input.isnumeric():
        cut_wire_index = int(wire_input)
        if cut_wire_index in range(1,6) :
          return cut_wire_index
        else:
          print(self.strings['error_wrong_wire'][self.language])
      elif wire_input == 'q':
        return 0
      else:
        print(self.strings['error_wrong_wire'][self.language])

  def print_wire_already_cut(self) -> None:
    """Affiche le message d'erreur du fil déjà coupé"""
    print(self.strings['wire_already_cut'][self.language])

  def print_round_won(self, name: str)-> None:
    won_message = self.strings['round_won'][self.language]
    won_message = won_message.replace('{name}', name)
    print(won_message)

  def print_round_lost(self) -> None:
    print(self.strings['round_lost'][self.language])

  def print_start_game(self, name: str)-> None:
    start_message = self.strings["start_game"][self.language]
    start_message = start_message.replace('{name}', name)
    print(start_message)
  
  def ask_replay(self) -> str:
    while True :
      replay_answer = input(self.strings['replay'][self.language]).lower()
      if replay_answer == 'y' or replay_answer == "n":
        return replay_answer
  
  def print_new_game(self, name) -> None:
    new_game_message = self.strings["new_game"][self.language]
    new_game_message = new_game_message.replace('{name}', name)
    print(new_game_message)
  
  def print_score(self, score) -> None:
    score_message = self.strings["new_game"][self.language]
    score_message = score_message.replace('{score}', str(score))
    print(score_message)
