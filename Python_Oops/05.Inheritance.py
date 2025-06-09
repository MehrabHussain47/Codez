# In python support multiple inhertance
class A:
    def __init__(self):
        print("Creating object for class A")
    def jump(self):
        print("I am jumping")

class AA(A):    # A is parent class and AA is child class
    def __init__(self): 
        print("Creating object for class AA")
        super().__init__()  # Will show the parent constructor's property
    def jump(self): # Method overriding
        print("Yay! I am jumping!!!") 

a = A()
# b = A()
c = AA()

a.jump()
c.jump()