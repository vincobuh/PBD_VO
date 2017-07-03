# define my car class

class Car:
	def __init__(self):
		self.__make = "Ferrari "
		self.__colour = "Red"
		self.__mileage = 0
		self.engineSize = "5.4L"
	
	
	def getMake(self):
		return self.__make
		
		
	def getColour(self):
		return self.__colour
		
	def getMileage(self):
		return self.__mileage
		
	def setMake(self, make):
		self.__make = make
		
	def setColour(self, colour):
		self.__colour = colour
		
	def setMileage(self, mileage):
		self.__mileage = mileage
		
	def move(self, distance):
		print("Moved " + str(distance) + "kms. ")
		self.__mileage = self.__mileage + distance
	
	def paint(self, colour):
		print("Getting a paint job - new colour is: " + colour)
		self.__colour = colour
		
		
class ElectricCar(Car):

	def __init__(self):
		Car.__init__(self)				# line 42 applies only in python 2.7
		self.__numberFuelCells = 1
		
	def getNumberFuelCells(self):
		return self.__numberFuelCells
		
	def setNumberFuelCells(self, value):
		self.__numberFuelCells = value
		
	




	
	

	



