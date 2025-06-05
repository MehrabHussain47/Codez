# If there are only two conditions.
n = int(input("Enter a number: "))

if n % 2 == 0:
    print(n, "is even number")
else:
    print(n, "is odd number")


# If there are more than two conditions.
age = int(input("Enter your age: "))

if age <= 18:
    print("You are a child.")
elif age < 35:
    print("You are young.")
else:
    print("You are old.")


# If there are more than two conditions.
age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age == 0:
    print("You are just born!")
elif age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
