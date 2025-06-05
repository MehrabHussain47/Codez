# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "CompSci"]
}

# Accessing values
print(student["name"])  # Output: John Doe
print(student["age"])   # Output: 21

# Adding a new key-value pair
student["grade"] = "A"
print(student)

# Updating an existing key-value pair
student["age"] = 22
print(student)

# Removing a key-value pair
del student["courses"]
print(student)

# Looping through keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "name" in student:
    print("Name is present in the dictionary")

# Dictionary length
print(f"Number of items in dictionary: {len(student)}")

# Storing data in dictionary d
d = {"Alex":16, "Bob":21} # here Alex is key and 16 is value

# Showing data of dictionary using index
print(d["Alex"])

# Showing the whole data of dictionary 
print(d)