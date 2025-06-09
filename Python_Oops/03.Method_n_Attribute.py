import time

class Car:
    # color = "White" # These 3 varibles are for default values.
    make = "Toyota"
    model = "Corolla"
    year = 2024

    # This method's variables are used for user defined values.
    def __init__(self, a, b, c="White"): # Constructor method
        print("Car is created!!!")  # object create korle ei method automatic call hoy
        self.make = a 
        self.model = b
        self.color = c

    # Car er object print korle basic information print hobe naile object er address print hobe 
    def __str__(self):
        return(f"{self.color}-{self.make}-{self.model}-{self.year}")
    
    def start_engine(self, t=2):
        self.year = 2025
        print("Starting engine...")
        time.sleep(t)
        print("Engine started! Ready to go!")

car1 = Car("Subaru", "Forester", "Bronze")
car1.color = "Blue"
car1.manufacture_year = 2020    # Manufacture Year attribute add korlam car1 er
car2 = Car("Toyota", "Prado", "White")
car2.color = "Red"
car3 = Car("Toyota", "Corolla")

print(car1.color, car1.make, car1.model, car1.manufacture_year)
print(car2.color, car2.make, car2.model, car2.year)
print(car3)

print("Before start engine", car1.year)
car1.start_engine()
print("After start engine", car1.year)
car2.start_engine(0)
car3.start_engine(5)