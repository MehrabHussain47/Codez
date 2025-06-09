class MyClass:
    value1 = 10 # Class variable

a_obj = MyClass()
print(type(a_obj))  # jei file theke program run kortesi shei file e MyClass naam er ekta class er object
print(a_obj.value1)
a_obj.value1 = 20   # Instance variable
print(a_obj.value1)
b_obj = MyClass()
print(b_obj.value1)