class car():   
        def __init__(self, make, name, year,):
            self.make = make
            self.name =name
            self.year = year
            self.reading = 0
        def get_descriptive_name(self):
            long_name ='this car was made in year '+ str(self.year) + ' and  this is a ' + self.make + ' ' + self.name
            return long_name.title()
        def odometer_reading(self):
            print("this car has " + str(self.reading) + " miles on it")
        def update_odometer_reading(self,odometer_reading):
            self.reading = odometer_reading