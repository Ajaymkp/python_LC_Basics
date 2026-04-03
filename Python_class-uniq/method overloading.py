from multipledispatch import dispatch

# addition
'''
@dispatch(int, int)

def add(a, b):
    print(a + b)  
def add(a, b):
    print(a*b)
add(2, 3)
'''
# cancatenation
'''
@dispatch(str, str)

def concat(a, b):
    print(a + b)
concat("Hello, ", "World!")
'''
# repeat string
'''
@dispatch(int,str)

def repeat_string(n, s):
    print(s * n)
repeat_string(3, "Hi! ")
'''
# method overloading in a class -- compile time polymorphism
'''
class A:
    @dispatch(str, str)
    def add(self, a, b):
        print(a + b)

    @dispatch(int, int)
    def add(self, a, b):
        print(a + b)

    @dispatch(int, str)
    def add(self, a, b):
        print(a*b)
a = A()
a.add(4, 5) 
a.add("Hello, ", "World!")
a.add(3, "Hi! ")
'''

# metjod overriding - run time polymorphism

class A:
    def cash(self):
        print("A")
class B(A):
    def cash(self):
        print("B")
b= B()
b.cash()