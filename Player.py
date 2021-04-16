import Element
import MapReader
class Player(Element.Element):
    
    def __init__(self):
        #Lorsqu'il n'y a pas encore de position trouvée, la position du joueur est setup par defaut en dehors de l'ecran pour qu'il ne soit pas visible. Ensuite, il récuperera les valeurs données.
        super().__init__(-5, -5)
        self.searchPos(MapReader.MapReader.arrayMap)

        
    def searchPos(self, map):
        for index, line in enumerate(map):
            try:
                pos_x = line.index('P')
                self.pos_x = pos_x
                self.pos_y = index
            except:
                pass
            