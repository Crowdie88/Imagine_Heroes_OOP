    
# Worldmap
class Map:
    def __init__(self, w, h, name):
        self.width = w
        self.height = h
        self.name = name
    def getWidth(self):
        return self.width
    def setWidth(self, new_Width):
        self.width = new_Width
    def getHeight(self):
        return self.height
    def setHeight(self, new_Height):
        self.height = new_Height
    def getName(self):
        return self.name
    def setName(self, new_Name):
        self.name = new_Name

# Celtic continent
Celtic_Continent = Map(500, 250, "Celtic Continent")

# Borsigwalde
Borsigwalde = Map(5, 5, "Borsigwalde")