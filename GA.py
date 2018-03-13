from TourManager import TourManager
from Tour import Tour
from Population import Population

import math
import random 

class GA:
    def __init__(self, tourmanager):
      #Parameters 
        self.tourmanager = tourmanager
        self.mutationRate = 0.015
        self.tournamentSize = 5
        self.elitism = True
      
    #Evolves a population over one generation   
    def evolvePopulation(self, pop):
            newPopulation = Population(self.tourmanager, pop.populationSize(), False)
            #If elitism is enabled, keep the best individual
            elitismOffset = 0
            if self.elitism:
                newPopulation.saveTour(0, pop.getFittest())
                elitismOffset = 1
            #Cross over the population
            #Loop over new pop's size, and create individuals from
            #The current population, where the current popuation acts
            #as 'parents' to the new population
            for i in range(elitismOffset, newPopulation.populationSize()):
                #Select parents
                parent1 = self.tournamentSelection(pop)
                parent2 = self.tournamentSelection(pop)
                #Cross them
                child = self.crossover(parent1, parent2)
                #Add child to new population
                newPopulation.saveTour(i, child)
                
          #Mutate the new population slightly for some new 'genetic material'
            for i in range(elitismOffset, newPopulation.populationSize()):
                self.mutate(newPopulation.getTour(i))
            return newPopulation
            
    #Applies crossover to a set of new parents and create offspring
    def crossover(self, parent1, parent2):
            #New child tour
        child = Tour(self.tourmanager)
            
        #Get start and end sub-tour positions ofr parent1's tour      
        startPos = int(random.random() * parent1.tourSize())
        endPos = int(random.random() * parent1.tourSize())
        
        #Loop and add the subtour from parent1 to the child
        for i in range(0, child.tourSize()):
            #If the start position is less than the end position
            if startPos < endPos and i > startPos and i < endPos:
                child.setCity(i, parent1.getCity(i))
            #If the start position is larger    
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.setCity(i, parent1.getCity(i))
            
        #Loop through parent2's city tour
        for i in range(0, parent2.tourSize()):
            #If the child doesn't have the city, add it
            if not child.containsCity(parent2.getCity(i)):
                #Find an open spot in the child's tour
                for ii in range(0, child.tourSize()):
                    #When an open spot is found, add city
                    if child.getCity(ii) == None:
                        child.setCity(ii, parent2.getCity(i))
                        break
      
        return child
      
    #Mutate a tour using swap mutation
    def mutate(self, tour):
        for tourPos1 in range(0, tour.tourSize()):
            #Apply mutation rate
            if random.random() < self.mutationRate:
                #get a second random position in the tour
                tourPos2 = int(tour.tourSize() * random.random())
                
                #Get cities at target position in tour
                city1 = tour.getCity(tourPos1)
                city2 = tour.getCity(tourPos2)
                
                #Swap them
                tour.setCity(tourPos2, city1)
                tour.setCity(tourPos1, city2)
   
    #Selects candidates for crossover
    def tournamentSelection(self, pop):
        #Create a tournament population
        tournament = Population(self.tourmanager, self.tournamentSize, False)
        #For each spot in the tournament, get a random candidate tour and add it
        for i in range(0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(randomId))
            
        #Get the most fit tour    
        fittest = tournament.getFittest()
        return fittest

