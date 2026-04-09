
#from multipledispatch import dispatch

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

# method overriding - run time polymorphism

# Different class same method name and same parameters it suppoorts python
'''
class A:
    def cash(self):
        print("A")
class B(A):
    def bike(self):
        print("B")
b= B()
b.cash()
'''
# method overriding in normal class
'''
class A:
    def cash(self):
        print("A")
class B(A):
    def cash(self):
        print("B")
b= B()
b.cash()
'''
# method overriding in multithreading
'''
class A():
    def display(self, m, n):
        print(m + n)
class B(A):
    def display(self, m, n):
        print(m * n)
b = B()
b.display("Hello ", 3)
'''






#______________-____________

# mehod overloading - compile time polymorphism


# method overriding - run time polymorphism

# Different class same method name and same parameters it suppoorts python

'''
class A:
    def cash(self):
        print("A")
class B(A):
    def bike(self):
        print("B")
b= B()
b.cash()

# method overriding in normal class

class A:
    def cash(self):
        print("A")
class B(A):
    def cash(self):
        print("B")
b= B()
b.cash()'''