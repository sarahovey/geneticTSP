class TourManager:
   #List to hold cities
   destinationCities = []
   
   #Add a city to list of destination cities
   def addCity(self, city):
      self.destinationCities.append(city)
      
   #Return a city at given index
   def getCity(self, index):
      return self.destinationCities[index]
   
   #Returns the number of cities to vitit
   def numberOfCities(self):
      return len(self.destinationCities)