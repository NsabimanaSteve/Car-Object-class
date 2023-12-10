from Person import *


class Car:
    """ A class to represent a Car."""
    
    def __init__(self, make, model, year, license_plate):
        """ The constructor initializes the car's make,model,year, licence_plate
            and passengers to the given values.
        """
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate
        self.driver = None
        self.front_passenger = None
        self.back_passenger1 = None
        self.back_passenger2 = None
        self.back_passenger3 = None

    def __str__(self):
        """ This method returns a string representation of a car.
        """
        return f"The car's information: make is: {self.make}, model is: {self.model}, year is: {self.year}, license plate is: {self.license_plate}"

    def set_driver(self, person):
        """This method takes in a reference to a Person object. If the person is above
           18, the car’s driver is set, replacing any driver that was there previously. The method then
           returns True. Otherwise, it returns False
        """
        
        if person.age > 18:
            self.driver = person
            return True
        else:
            return False
    def has_driver(self):
        """This method returns whether or not the car currently has a driver (i.e. the
            driver instance variable is not None)"""
        
        return self.driver is not None #returns True if there is a Driver 

    def add_passenger(self, person):
        """ This method tries to
            put the passenger in one of the passenger slots (frontSeatPassenger, backSeatPassenger1,
            backSeatPassenger2, or backSeatPassenger3) and returns whether or not it was successful in
            doing so.""" 
        if self.front_passenger is None and person.age >= 10:
            self.front_passenger = person
            return True
        elif self.back_passenger1 is None:
            self.back_passenger1 = person
            return True
        elif self.back_passenger2 is None:
            self.back_passenger2 = person
            return True
        elif self.back_passenger3 is None:
            self.back_passenger3 = person
            return True
        else:
            return False

    def has_passengers(self):
        """This method returns whether or not the car has at least one
            passenger.
        """
        return (
            self.front_passenger is not None
            or self.back_passenger1 is not None
            or self.back_passenger2 is not None
            or self.back_passenger3 is not None
        )

    def get_num_occupants(self):
        """This method returns the current number of occupants in the car
            (including the driver)
        """
        count = 0
        if self.driver is not None:
            count += 1
        if self.front_passenger is not None:
            count += 1
        if self.back_passenger1 is not None:
            count += 1
        if self.back_passenger2 is not None:
            count += 1
        if self.back_passenger3 is not None:
            count += 1
        return count

    def get_num_passengers(self):
        """ This method returns the current number of passengers (not
            including the driver)"""
        if self.driver is not None:
            return self.get_num_occupants() - 1
        else:
            return 0
        

    def is_empty(self):
        """ This method which returns whether or not the car is empty (has no driver or
            passengers)
        """
        return self.get_num_occupants() == 0

    def is_full(self):
        """This method returns whether or not the car is full (all spots for the driver and
           passenger are taken)
        """
        return self.get_num_occupants() == 5 #In case there are five seat

    def list_riders(self):
        
        result = []
        if self.driver:
            result.append(f"Driver: {self.driver.name} (Age: {self.driver.age})")
        if self.front_passenger:
            result.append(f"Front Seat Passenger: {self.front_passenger.name} (Age: {self.front_passenger.age})")
        if self.back_passenger1:
            result.append(f"Back Seat Passenger 1: {self.back_passenger1.name} (Age: {self.back_passenger1.age})")
        if self.back_passenger2:
            result.append(f"Back Seat Passenger 2: {self.back_passenger2.name} (Age: {self.back_passenger2.age})")
        if self.back_passenger3:
            result.append(f"Back Seat Passenger 3: {self.back_passenger3.name} (Age: {self.back_passenger3.age})")
            
        print(result)

# Create people
if __name__=="__main__":
    driver=Person("Sogho",23)
    person1 = Person("Steve", 25)
    person2 = Person("Eli", 30)
    person3 = Person("Innocent", 16)
    person4 = Person("Zainabu", 22)

    # Create a car
    car = Car("Honda", "Accord", 2022, "XYZ789")

    # Test Car methods
    print(car)
    print("Set Driver:", car.set_driver(driver)) # True
    print("Has Driver:", car.has_driver())  # True
    print("Add Passenger:", car.add_passenger(person1))  # True
    car.add_passenger(person2)
    car.add_passenger(person3)
    car.add_passenger(person4)

    print("Has Passengers:", car.has_passengers())  # True
    print("Get Num Occupants with Driver:", car.get_num_occupants())  
    print("Get Num Passengers without Driver:", car.get_num_passengers())  

    print("Is Empty:", car.is_empty())  # False
    print("Is Full:", car.is_full())  # False
    print()
    print("List Riders:")
    car.list_riders()

