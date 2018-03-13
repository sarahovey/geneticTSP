#Implementation of a genetic algorithm to solve TSP
#For Analysis of Algorithms class research project
#References/sources:
#http://www.theprojectspot.com/tutorial-post/applying-a-genetic-algorithm-to-the-travelling-salesman-problem/5
#http://www.theprojectspot.com/tutorial-post/creating-a-genetic-algorithm-for-beginners/3
#https://pdfs.semanticscholar.org/010b/545848cfd29fe6e83987d494fdd00b486229.pdf 
#https://gist.github.com/turbofart/3428880 

#Outputs to a text file per professor specification
#Line 1: distance
#Lines 2-n: cities in the order they appear in the best tour

import math
import random

from City import City
from TourManager import TourManager
from Tour import Tour
from Population import Population
from GA import GA
            
#Text file format
#Each line = city name, then 3 ints
#Int 1:city ID
#int 2: x coord
#int 2: y coord

#Get data from file
cities = []
with open('cities.txt', 'r') as file:
    line = file.readline()
    while line:
        #Stick current line into new list
        cur_line = line.split()
        if len(cur_line) > 0:
            cities.append(cur_line)
        line = file.readline()

#Now that we have all the data, we can parse and format it
for i in range(len(cities)):
    if len(cities[i]) != 3:
        raise Exception('invalid formatting for City in text file')

#From the list of lines, make a list of City objects
cities = [City.fromList(cty) for cty in cities]

#Initialize a TourManager object and add cities to its list of destinations
tourmanager = TourManager()
for i in range(len(cities)):
    tourmanager.addCity(cities[i])
    
#Init a population of individual tours
pop = Population(tourmanager, len(cities), True);

#print intitual distance
print("Initial distance: " + str(pop.getFittest().getDistance()))

#Construction zone:

#Evolve population for 100 generations
ga = GA(tourmanager)
pop = ga.evolvePopulation(pop)
for i in range(0, 100):
    pop = ga.evolvePopulation(pop)

#Final results
finalDist = str(pop.getFittest().getDistance())
#Returns a tour object
bestTour = pop.getFittest()
print("Finished!")
print("Final distance: " + finalDist)
print("Best tour/solution:")
print(bestTour)

#Write to file
with open('geneticTSP.out', 'a') as fOut:
    #format sorted values for writing       
    fOut.write("%s\n" % (finalDist))
    for i in range(len(bestTour)):
        fOut.write("%s\n" % (bestTour.getCity(i).cid))
