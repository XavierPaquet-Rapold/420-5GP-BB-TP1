class wire:
  """Classe representant un lien entre une capital et un pays"""

  def __init__(self, country: str, capital: str, is_bomb: bool) -> None:
    """Constructeur d'un fil"""
    self.country = country
    self.capital = capital
    self.is_bomb = is_bomb
    self.is_cutted = False

  def __str__(self) -> str:
    """Affichage d'un fil"""
    if self.is_cutted:
      return "{0} ~~/ /~~ {1}".format(self.country, self.capital)
    return "{0} ~~~~~~~ {1}".format(self.country, self.capital)
  
  def is_cutted(self) -> bool:
    """Retourne si le cable a ete coupe"""
    return self.is_cutted
  
  def is_bomb(self) -> bool:
    """Retourne si le lien est une bombe"""
    return self.is_bomb

  def cut_cable(self) -> None:
    """Coupe le cable"""
    self.is_cutted = True
