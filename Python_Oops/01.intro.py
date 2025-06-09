# Object oriented programming

# Object has two characteristics: 
# 1.Property => taka.value = 100, taka.type = "Note"
# 2.Method  => taka.double()


# li = [1,2,3]    # Object/Instance
# print(type(li)) # li is an object of list class
# print(dir(li))  # we can see li object's properties
# li.reverse()    # reverse() is list class's method
# print(li)


# x = 6
# print(dir(x))   # double underscore holo magic method/ dunder method


# class MyClass:
#     value1 = 10 # Class variable

# a_obj = MyClass()
# print(type(a_obj))  # jei file theke program run kortesi shei file e MyClass naam er ekta class er object
# print(a_obj.value1)
# a_obj.value1 = 20   # Instance variable
# print(a_obj.value1)
# b_obj = MyClass()
# print(b_obj.value1)

class Car:
    color = "White"

car1 = Car()
car2 = Car()
car3 = Car()
