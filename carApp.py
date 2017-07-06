from car import Car, ElectricCar


my_car = Car()								#Class Car or my_car

print my_car.engineSize  	#Engine size is public (ie has no __)and will be printed

print my_car.getMake()   	#This will print if i add [def getMake(self): return self.__make]
#print my_car.__make     	#Error message bc "make" is private (ie has __)

print my_car.getColour()
#print my_car.__colour	 	#Will not print "same reason in line 27

print my_car.getMileage()
#print my_car.__mileage  	#Will not print "same reason in line 27

my_car.engineSize = ("2.5L")
print my_car.engineSize

my_car.setMake("BMW")
print my_car.getMake()

my_car.setColour("Silver")
print my_car.getColour()

my_car.setMileage(50)
print my_car.getMileage()

my_car.move(10)
print my_car.getMileage()

my_car.paint("Blue")
print my_car.getColour()

electric_car = ElectricCar()				#Class ElectricCar or electric_car

print electric_car.getNumberFuelCells()

electric_car.move(20)
print electric_car.getMileage()

#my_car.getNumberFuelCells()		#error bc my_car does not have NumberofFuels