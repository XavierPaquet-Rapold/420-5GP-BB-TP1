import os
import json

class tools:
  """Classe contenant les affichages"""
  def __init__(self, language: str) -> None:
    if language != 'fr' and language != 'en':
      raise Exception('Language not supported')
    self.language = language
    with open('./Etape4-5/strings.json', 'r') as strings_file:
      self.strings = json.load(strings_file)
    
  def ask_name(self) -> str:
    while True:
      name = input(self.strings['ask_name'][self.language])
      if name.isalpha():
        return name
      else:
        print(self.strings['error_name'][self.language])
  
  @staticmethod
  def ask_language() -> str:
    """Demander la langue du jeu"""
    while True:
      language = input("Veuillez indiquer la langue de votre choix ou quitter avec 'q'\n" +
        "Please indicate the language of your choice (en, fr) or quit with 'q': ").lower()
      if(language == 'fr' or language == 'en' or language == 'q'):
        return language
      else:
        print("Merci d'entrer 'fr' ou 'en' | Please enter 'en' or 'fr'")