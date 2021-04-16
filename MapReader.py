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
    number_X = 0
    number_0 = 0
    verif_caractere = False
    #On verifie le nombre de P dans la map
    for item in re.finditer("P", self.map):
          number_P += 1
    if number_P > 1:
          print(f"Il y a trop de joueurs !")
          return False
    elif number_P < 1:
          print(f"Il n'y a pas assez de joueur !")
          return False
    
    for item in re.finditer("^(#|X|0|P)*$", self.map.rstrip()):
          verif_caractere = True
    
    if verif_caractere != True:
          print(f"Cette map contient des caracteres non valides")
          return False
        
      
    # Avec un seul Joueur -> Par un P -> sinon erreur
    # La map doit contenir que des espaces \n des #,X,0,P
    # Autant de boxe que d'emplacement -> une box X et un emplacement O
    # Nous devons prendre une map en paramètre qui doit être fermée!(toutes tailles possibles)
    return self.map