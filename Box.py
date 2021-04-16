import Element
import MapReader

class Box(Element.Element):
    
    def __init__(self):
        super().__init__(-5, -5)
        self.searchPos(MapReader.MapReader.arrayMap)
        
    def searchPos(self, map):
        for index, line in enumerate(map):
            try:
                pos_x = line.index('X')
                self.pos_x = pos_x
                self.pos_y = index
            except:
                pass

