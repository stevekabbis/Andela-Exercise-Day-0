class Car(object):

    speed = 0

    def __init__(self, name='General', model="GM", car_type="saloon"):
        self.name = name
        self.model = model
        self.type = car_type
        if self.name in ('Toyota', 'Nissan'):
          self.num_of_doors = 2
        else: self.num_of_doors = 4
        if self.type == 'saloon':
          self.num_of_wheels = 4
        else: self.num_of_wheels = 8

    def is_saloon(self):
        if self.type == 'saloon':
            return True

    def drive(self, n):
        if self.name == 'DRIVER':
            self.speed = 77
        else:
            self.speed = 10 ** n
        return self
