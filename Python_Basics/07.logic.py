num = input("Enter a number: ")
num = int(num) # without this will give you error cause in input() we can only input string

if num % 2 == 0:
    print(num, "is even number") # use tab to avoid indentation error in this block
else:
    print(num, "is odd number")