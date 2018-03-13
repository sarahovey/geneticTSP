import math
import random

from TourManager import TourManager
from City import City

class Tour:
    def __init__(self, tourmanager, tour=None):
        self.tourmanager = tourmanager
        self.tour = []
        self.fitness = 0.0
        self.distance = 0
        if tour is not None:
            self.tour = tour
        else:
            #builds a tour from the list of destination cities
            for i in range(0, self.tourmanager.numberOfCities()):
                self.tour.append(None)
   
    def __len__(self):
        return len(self.tour)
    
    def __getitem__(self, index):
        return self.tour[index]
    
    def __setitem__(self, key, value):
        self.tour[key] = value
    
    def __repr__(self):
        geneString = "|"
        for i in range(0, self.tourSize()):
            geneString += str(self.getCity(i)) + "|"
        return geneString
   
   #generates a tour by shuffling the order of destination cities
    def generateIndividual(self):
        for cityIndex in range(0, self.tourmanager.numberOfCities()):
            self.setCity(cityIndex, self.tourmanager.getCity(cityIndex))
        random.shuffle(self.tour)
   
    def getCity(self, tourPosition):
        return self.tour[tourPosition]
   
   #Sets a city to a position on the tour
    def setCity(self, tourPosition, city):
        self.tour[tourPosition] = city
        self.fitness = 0.0
        self.distance = 0
   
   #Returns the fitness of the tour
    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1/float(self.getDistance())
        return self.fitness
   
   #get the total distance of the tour
    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for cityIndex in range(0, self.tourSize()):
                fromCity = self.getCity(cityIndex)
                destinationCity = None
                if cityIndex+1 < self.tourSize():
                    destinationCity = self.getCity(cityIndex+1)
                else:
                    destinationCity = self.getCity(0)
                tourDistance += fromCity.distanceTo(destinationCity)
            self.distance = tourDistance
        return self.distance
   
   #Returns the size of the tour
    def tourSize(self):
        return len(self.tour)
    
    #Check if the tour contains a city    
    def containsCity(self, city):
        return city in self.tour