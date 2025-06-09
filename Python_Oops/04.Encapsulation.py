# Public Members
class Public:
    def __init__(self):
        self.name = "John"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible


# Protected Members
class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()


# Private Member
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
# print(obj.__salary)  # Raises AttributeError