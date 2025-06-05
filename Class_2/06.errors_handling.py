# Error handling if I know the error
a = 2
b = 0 
# print(a/b) # ZeroDivisionError
try:
    print(a/b)
except ZeroDivisionError:
    print("Error: division by zero")

# Error handling if I don't know the error
a = 2
b = 0 
try:
    print(a/b)
except:
    print("Error: division by zero")

# Error handling using function
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        return result
    finally:
        print("Execution completed.")

# Test cases
print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print an error message
print(divide(10, 'a'))  # Should print an error message