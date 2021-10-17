import json
import os


class tools:
  """Classe contenant les affichages"""
  def __init__(self, language: str, dir_path: str) -> None:
    """Constructeur"""
    if language != 'fr' and language != 'en':
      raise Exception('Language not supported')
    self.language = language
    with open(os.path.join(dir_path, 'public/strings.json'), 'r') as strings_file:
      self.strings = json.load(strings_file)

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

  def ask_name(self) -> str:
    """Affichage de la demande du nom"""
    while True:
      name = input(self.strings['ask_name'][self.language])
      if name.isalpha():
        return name
      else:
        print(self.strings['error_name'][self.language])

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
  
  def ask_replay(self) -> bool:
    """Demander si le joueur veut rejouer au jeu"""
    while True :
      replay_answer = input(self.strings['replay'][self.language]).lower()
      if replay_answer == 'o' or replay_answer == "n":
        return False if replay_answer == 'n' else True

  def get_message(self, key: str, pattern : str = '', replace: str = '') -> str :
    """Recevoir un message à afficher"""
    message = self.strings[key][self.language]
    message = message.replace(pattern, replace)
    return message
