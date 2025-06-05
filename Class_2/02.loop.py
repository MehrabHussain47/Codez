# for loop
for i in range(20):
    print(i)

# for loop using intial and terminal
for i in range(1, 21):
    print(i)

# loop using increment
for i in range(1, 21, 3):   # Going through like 3 steps which is third limit
    print(i)

# loop using decrement
for i in range(20, 0, -1):    # initial 20 which is first limit and second limit is exclusive
    print(i)

for i in range(20, -1, -2):
    print(i)

# we can implies multiplication to i block
for i in range(1, 21):
    print(i*2)

# For loop example
print("For loop example:")
for i in range(5):
    print(i)

# while loop
print("\nLoop-1")
i = 1
while(i <= 20):
    print(i)
    i = i + 1

# same but increment steps will be 3
print("\nLoop-2")
i = 1
while(i <= 20):
    print(i)
    i = i + 3   

# While loop example
print("\nWhile loop example:")
count = 0
while count < 5:
    print(count)
    count += 1

# Looping through a list
print("\nLooping through a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with break
print("\nLoop with break:")
for i in range(10):
    if i == 5:
        break
    print(i)

# break keyword
print("\nBreak")
for i in range(0, 10):
    print(i)
    if i == 5:
        break

# Loop with continue
print("\nLoop with continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# continue keyword
print("\nContinue")
for i in range(0, 10):
    if i == 5:
        continue
    print(i)
    