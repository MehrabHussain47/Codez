# User defined function


# Function-1
def add_3(n):
    return n + 3

x = 5
y = add_3(x)
print(x, y)


# Function-2
def greetings(name):
    print("Hello,", name)

greetings("Sumon")
greetings("Ripon")
greetings("Sakib")


# Function-3
def f(n):   # ei n holo ei function er local variable
    n = 10
    print(n)

n = 5
f(n)
print("n =", n)


# Function-3
def greetings(name):
    print("Hello,", name)

n = input("Enter a name: ")
greetings(n)

