import os
import re #import pour expression reguliere
import sys

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
    
    number_P = 0
    #On verifie le nombre de P dans la map
    for item in re.finditer("P", self.map):
          number_P += 1
    if number_P > 1:
          print(f"Il y a trop de joueurs !")
          return False
    elif number_P < 1:
          print(f"Il n'y a pas assez de joueur !")
          return False
          
      
    # Avec un seul Joueur -> Par un P -> sinon erreur
    # Autant de boxe que d'emplacement -> une box X et un emplacement O
    # La map doit contenir que des espaces \n des #,X,0,P
    return self.map