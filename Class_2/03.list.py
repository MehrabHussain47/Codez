# Introduction to Lists in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements in a list
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])

# Modifying elements in a list
fruits[1] = "blueberry"
print("Modified fruits:", fruits)

# Adding elements to a list
fruits.append("orange")
print("Fruits after adding an element:", fruits)

# Removing elements from a list
fruits.remove("cherry")
print("Fruits after removing an element:", fruits)

# Iterating through a list
print("Iterating through the list:")
for fruit in fruits:
    print(fruit)

# List length
print("Number of fruits:", len(fruits))

# List slicing
print("First two fruits:", fruits[:2])
print("Last two fruits:", fruits[-2:])

# List comprehension
squares = [x**2 for x in range(10)]
print("Squares of numbers from 0 to 9:", squares)

# Storing data in list l
l = [-1,1,2,2.3,3,4,5,6,7]

# Showing data of list index wise
print(l[0])
print(l[1])
print(l[4])
print(l[5])

# Showing data of list index wise using loop
for i in range(0, 5):
    print(l[i])

for i in range(0, len(l)):
    print(l[i])