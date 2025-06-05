# Multiplication Table using function
def print_multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n = input("Enter a number: ")
n = int(n)
print("Multiplication Table for", n, ":")
print_multiplication_table(n)

# Creating Multiplication Table
n = input("Enter a number: ")
n = int(n)
print("Multiplication Table for", n, ":")
for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# print("5 x 1 = 5")
# print("5 x 2 = 10")
# print("5 x 3 = 15")
# print("5 x 4 = 20")
# print("5 x 5 = 25")
# print("5 x 6 = 30")
# print("5 x 7 = 35")
# print("5 x 8 = 40")
# print("5 x 9 = 45")
# print("5 x 10 = 50")