import math
import random

#City class
class City:
    def __init__(self, cid, x, y):
        self.cid = cid
        self.x = x
        self.y = y

    def getX(self):
        return int(self.x)
        
    def getY(self):
        return int(self.y)
        
    def getCid(self):
        return self.cid
    
    #Return distance from self to another city    
    def distanceTo(self, city):
        xDist = abs(self.getX()- city.getX())
        yDist = abs(self.getY()- city.getY())
        distance = math.sqrt((xDist*xDist)+(yDist*yDist))
        return distance
        
    @staticmethod
    def fromList(le):
        if len(le) !=3:
            raise Exception('Invalid city line entry')
        return City(le[0], le[1], le[2])
        
    def __str__(self):
        return "City(id: {}, x: {}, y: {})".format(self.cid, self.x, self.y)
        
    def __repr__(self):
        return self.__str__()