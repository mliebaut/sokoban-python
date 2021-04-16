import os
import re #import pour expression reguliere
import sys

class MapReader:
  def __init__(self, mapPath):
    self.mapPath = mapPath
    self.map = None
    self.arrayMap = None
    self.readMap()
  
  def readMap(self):
    with open(self.mapPath, 'r', encoding='utf-8') as file:
      self.map = ''.join(file)
      return file.readlines()

  def verifyMap(self):
    
    number_P = 0
    number_X = 0
    number_O = 0
    
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

    #On verifie qu'il n'y a bien que les caracteres autorisés
    for item in re.finditer("^(#|X|O|P|\s)*$", self.map.rstrip()):
          verif_caractere = True

    if verif_caractere != True:
          print(f"Cette map contient des caracteres non valides")
          return False

    #On verifie qu'il y autant de box que d'emplacement
    for item in re.finditer("(O)|(X)", self.map):
          if item.group() == 'O':
              number_O += 1
          else:
              number_X += 1
    if number_O != number_X:
          print(f"Il faut autant de box que d'emplacements !")
          return False

    #On verifie que la map est fermée
    self.arrayMap = self.map.split('\n')
    self.arrayMap = [re.sub("^(\s*)[^#]", '', item) for item in self.arrayMap]

    for i in enumerate(self.arrayMap):
          if i[0] == 0 or len(self.arrayMap) - 1 == i[0]:
                if re.search("[^#]", self.arrayMap[i[0]]):
                      print(i, re.match("[^#]", self.arrayMap[i[0]]))
                      print(f"Cette map n'est pas valide: Il faut une map avec les bordures fermées")
                      return False
          else:
                if re.match("^#.*#$", self.arrayMap[i[0]]) == None:
                      print(i, re.match("^#.*#$", self.arrayMap[i[0]]))
                      print(f"Cette map n'est pas valide: Il faut une map avec les bordures fermées")
                      return False
    return True
  
  def displayMap(self, stdscr):
        pos_y = 0
        
        for line in self.arrayMap:
              pos_y += 1
              stdscr.addstr(pos_y, 10, line)
              
              
    