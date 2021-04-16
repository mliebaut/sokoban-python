import MapReader

class Element:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.max_x = None
        self.max_y = None
        

    def moveUp(self):
        if self.pos_y > 0:
            self.pos_y += 1
        
    def moveDown(self):
        if self.pos_y < self.max_y:
            self.pos_y -= 1
        
    def moveRight(self):
        if self.pos_x < self.max_x[self.pos_y]:
            self.pos_x += 1
        
    def moveLeft(self):
        if self.pos_x > 0:
            self.pos_x -= 1
        
    def maxMin():
        self.max_x = []
        map = MapReader.MapReader().getStaticMap()
        
        self.max_y = len(map) - 1
        
        for line in map:
            self.max_x.append(len(line))
        