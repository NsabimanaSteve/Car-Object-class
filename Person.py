class Person:
    """ A class to represent a person."""

    def __init__(self, n='', a=0):
        """ The constructor initializes the person's name and age to
            the given values.
        """
        self.name = n
        self.age = a

    def change_name(self, new_name):
        """ This method changes the person's name to the given value.
        """
        self.name = new_name

    def get_older(self):
        """ This method increases the person's age by 1 year.
        """
        self.age += 1

    def allowed_to_drive(self):
        """ This method returns whether or not the person is allowed to drive.
        """
        # return self.age >= 18
        if self.age >= 18:
            return True
        else:
            return False

    def __str__(self):
        """ This method returns a string representation of a person.
        """
        # alternatives
        #return "Person with name " + self.name + " and age " + self.age
        #return f"Person with name {self.name} and {self.age}"
        return "Person with name {} and age {}".format(self.name, self.age)


if __name__ == "__main__":
    person1 = Person("Ayorkor", 23)
    person2 = Person("Chudah", 17)
    person3 = Person("Chudah", 17)

    print("I have created three instances of the Person class")
    print("person1 string representation =", person1)
    print("person2 string representation =", person2)
    print("person3 string representation =", person3)

    print("\nTheir types are:")
    print("type(person1) =", type(person1))
    print("type(person2) =", type(person2))
    print("type(person3) =", type(person3))
    print(person1.allowed_to_drive())


