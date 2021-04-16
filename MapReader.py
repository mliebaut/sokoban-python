import os

class MapReader:
  def __init__(self, mapPath):
    self.mapPath = mapPath
    self.map = None
    self.readMap()
  
  def readMap(self):
    with open(self.mapPath, 'r', encoding='utf-8') as file:
      self.map = ''.join(file)
      return file.readlines()

  def verifyMap(self):
    # Avec un seul Joueur -> Par un P -> sinon erreur
    # Autant de boxe que d'emplacement -> une box X et un emplacement O
    # La map doit contenir que des espaces \n des #,X,0,P
    return self.map