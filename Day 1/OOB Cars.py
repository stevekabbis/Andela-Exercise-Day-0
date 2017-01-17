#A Real life Application of OOP
class car:
  def __init__(self, name):    # This will construct the class
    self.name = name

class type_1(car):     #create another class that inherits from car
  def type(self):
    return "convertible"
    
class type_2(car):    #Another class that also inherits from car
  def type(self):
    return "4 wheel drive"
    
    
cars= [type_1("Ferrari Enzo"), type_2("Porsche Arcea")]

for car in cars:
  print(car.name +" " +car.type())
