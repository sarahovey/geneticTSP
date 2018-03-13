import math
import random

from Tour import Tour

class Population:
    
    def __init__(self, tourmanager, populationSize, initialize):
        self.tours = []
        for i in range(0, populationSize):
            self.tours.append(None)
        
        if initialize:
            for i in range(0, populationSize):
                newTour = Tour(tourmanager)
                newTour.generateIndividual()
                self.saveTour(i, newTour)
                
    def __setitem__(self, key, value):
        self.tours[key] = value
        
    def __getitem__(self, index):
        return self.tours[ndex]
        
    def saveTour(self, index, tour):
        self.tours[index] = tour
        
    def getTour(self, index):
        return self.tours[index]
    
    def getFittest(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.getFitness() <=self.getTour(i).getFitness():
                fittest = self.getTour(i)
        return fittest
        
    def populationSize(self):
        return len(self.tours)
