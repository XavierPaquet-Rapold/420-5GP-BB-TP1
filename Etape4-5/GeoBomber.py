from typing import Dict
import os
from Tools import tools
from Wire import wire

def read_file() -> str:
  with open(os.path.join(os.getcwd(), 'liste-197-etats-2020.csv')) as country_file:
    file_content = country_file.readlines()
    #supprimer la première ligne, car ce sont les titres de chaque colonne
  del file_content[0]
  return file_content

def main():
  MIN_BOMB = 1
  MAX_BOMB = 4
  NB_WIRE = 5
  language = tools.ask_language()
  if language == 'q':
    return
  user_query_tool = tools(language)
  user_query_tool.ask_name()

if __name__ == "__main__":
  try:
    main()
  except:
    print("Erreur fatale, veuillez réessayer")