# Print 0 to 9
for i in range(10):
    print(i)

# Print 1 to 9
for i in range(1, 10):
    print(i)

# Print 1 to 7 via 3 steps
for i in range(1, 10, 3):
    print(i)

# Print 10 to 1
for i in range(10, 0, -1):
    print(i)

# Print 0 to 99
num = 100
for x in range(num):
    print(x, end=" ")

# pattern
for i in range(7):  # "*" * 5 => "*****"
    print("*" * (i+1))  # this print will run exactly 7 times.