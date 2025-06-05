# Basic Python Functions

# A simple function that prints a greeting message
def greet():
    print("Hello, welcome to learning Python functions!")

# A function that takes a name as an argument and prints a personalized greeting
def greet_person(name):
    print(f"Hello, {name}! Welcome to learning Python functions!")

# A function that takes two numbers as arguments and returns their sum
def add_numbers(a, b):
    return a + b

# A function that takes a list of numbers and returns their average
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

# A function that demonstrates the use of default arguments
def greet_with_default(name="Student"):
    print(f"Hello, {name}! Welcome to learning Python functions!")

# A function that demonstrates the use of keyword arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

greet()
greet_person("Alice")
print(f"Sum of 3 and 5 is: {add_numbers(3, 5)}")
print(f"Average of [1, 2, 3, 4, 5] is: {calculate_average([1, 2, 3, 4, 5])}")
greet_with_default()
greet_with_default("Bob")
describe_person(name="Charlie", age=30, city="New York")

# creating a function test
def test():
    print("test")

test()

# Creating a function test2 for checking if it is odd or even number
def test2(num):
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")
        
test2(23)

# Creating a function test3 for checking if it is odd or even number by input from user
def test3(num):
    if num % 2 == 0:
        print(num, "is even number")
    else:
        print(num, "is odd number")
        
n = int(input("Enter a number: "))
test3(n)

# Creating a function test4 for checking if it is odd or even number by input from user and return output
def test4(num):
    if num % 2 == 0:
        return f"{num} is even number"
    else:
        return f"{num} is odd number"
        
n = int(input("Enter a number: "))
print(test4(n))