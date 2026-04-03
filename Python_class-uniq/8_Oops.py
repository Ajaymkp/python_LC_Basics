
#                                                      Date: 26-03-2026

# OOPS 

# class is a blueprint of object and 
## logical entity
### class can create multiple objects

# Objects

# object is an instance of class
## physical entity

#
# self refer to the current object
'''
class Aizen:
    def detail(self):
        print("Yokoso")
        print(id(self))
x=Aizen()                         # here x is an object and it has same id as self
x.detail()
print(id(x))

y=Aizen()
y.detai()
print(id(y))
'''

# not working
'''
class A:
    def func(self,name):
        return name
x=A()
print(x.func())
print(A()__dict__)
'''
#
'''
class A:
    def func(self,name):
        return name
x=A()
print(x.func("Aizen"))
'''
# 
'''
class A:
    def func(self,name):
        self.name=name
    def display(self):
        print(self.name)
x=A()
x.func("Gin")
x.display()         # it is the one call function to print Gin
print(x.__dict__)
'''

# constructor

# __init__ -- to create a constructor.
## init method is a special method in python which is used to
## --initialize the object of the class.
'''
class A:
    def __init__(self,name):
        print(name)
A("Gin")
#x=A("Ichimaru")
'''

#  if __init__ there we don't need to call the function to the read def
'''
class A:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
x=A("Ruken")
x.display()         # it is the one call function to print Ruken
print(x.__dict__)
'''


# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 27-03-2026

#  eg for next one
'''
class A:
    def func(self,a,b):
        print(a+b)
x=A()
x.func(10,20)
'''
# calling outside def variable -- (self.z)
'''
class A:
    z=30
    def func(self,a,b):
        print(a+b+self.z)
x=A()
x.func(10,20)
'''
# calling func arguments in another display function
'''
class A:
    def func(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a+self.b)
x=A()
x.func(10,20)
x.display()
'''

# same but using init method
'''
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a*self.b)
x=A(10,20)
x.display()
'''
# without argument in init but also same

'''
class A:
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):
        print(self.a*self.b)
x=A()
x.display()
'''

# destructor
# init is create and del is delete the object
'''
class A:
    def __init__(self):
        print("created")
    def __del__(self):
        print("deleted")
x=A()
del x
'''
# same but inverse the place

'''
class A:
    def __del__(self):
        print("deleted")
    def __init__(self):
        print("created")
x=A()
del x        
'''
#___________________________________________________________________________________________________________________

# Inheritance

# Single inheritance:
# class is derived from single parent class

'''
class dad:
    def cash(self):
        print("dad's cash")
class son(dad):
    def bike(self):
        print("son's bike")
d=dad()
d.cash()

s=son()
s.bike()
s.cash()
'''

# Multiple inheritance:

# class is derived from two or more parent class
'''
class dad:
    def cash(self):
        print("dad's cash")
class mom:
    def phone(self):
        print("mom's phone")
class son(dad,mom):
    def bike(self):
        print("son's bike")
        
d=dad()
d.cash()

m=mom()
m.phone()

s=son()
s.bike()
s.cash()
s.phone()
'''

# Multilevel inheritance:

# a class is derived from a child class which is derived from a parent class
'''
class grand:
    def land(self):
        print("grandpa's land")
class dad(grand):
    def cash(self):
        print("dad's cash")

class son(dad):
    def bike(self):
        print("son's bike")
        
g=grand()
g.land()

d=dad()
d.cash()
d.land()

s=son()
s.bike()
s.cash()
s.land()
'''
# hierarchical inheritance:

# two or more class is derived from a single parent class
'''
class dad:
    def cash(self):
        print("dad's cash")
class son(dad):
    def bike(self):
        print("son's bike")
class daughter(dad):
    def gold(self):
        print("daughter's ")

d=dad()
d.cash()

s=son()
s.bike()
s.cash()

d=daughter()
d.gold()
d.cash()
'''

# hybrid inheritance

# using two or more inheritance 

'''
class dad:
    def cash(self):
        print("dad's cash")
class mom:
    def  phone(self):
        print("mom's phone")
class daughter(dad,mom):
    def gold(self):
        print("daughter's gold")
class sonInLaw(daughter):
    def house(self):
        print("sonInlaw's house")

d=dad()
d.cash()

m=mom()
m.phone()

d=daughter()
d.gold()
d.cash()
d.phone()

s=sonInLaw()
s.house()
s.gold()
s.cash()
s.phone()
'''



# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 28-03-2026

# saturday -- assessment and mock

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 29-03-2026
#  sunday -- Holiday

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 30-03-2026

# mro -- Method Resolution order

## c3 linearization

# mro of F = FDBECAO
'''
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")       
class C(A):
    def __init__(self):
        print("C")
class D(B):
    def __init__(self):
        print("D")
class E(C):
    def __init__(self):
        print("E")
class F(D,E):
    def __init__(self):
        print("E")

f=F()
print(F.__mro__)
'''
# mro of F = FDEBCAO
 
'''
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")       
class C(A):
    def __init__(self):
        print("C")
class D(B,c):
    def __init__(self):
        print("D")
class E(B,C):
    def __init__(self):
        print("E")
class F(D,E):
    def __init__(self):
        print("E")

f=F()
print(F.__mro__)
'''

# mro of F == FDBAECO
'''
class A:
    def __init__(self):
        print("A")
class B:
    def __init__(self):
        print("B")       
class C:
    def __init__(self):
        print("C")
class D(B):
    def __init__(self):
        print("D")
class E(C):
    def __init__(self):
        print("E")
class F(D,A,E):
    def __init__(self):
        print("E")

f=F()
print(F.__mro__)
'''

# super().  mthod single
'''
class Dad():
    def cash(self):
        print("Dad's cash")
class Son(Dad):
    def cash(self):
        super().cash()
        print("Son's cash")
d=Dad()
d.cash()
s=Son()
s.cash()
'''
# same but reverse order for calling

'''
class Dad():
    def cash(self):
        print("Dad's cash")
class Son(Dad):
    def cash(self):
        print("Son's cash")
        super().cash()
d=Dad()
d.cash()
s=Son()
s.cash()
'''

# multiple 
'''
class Dad():
    def cash(self):
        print("Dad's cash")
        
class Mom():
    def cash(self):
        print("Mom's cash")
        super().cash()
class Son(Mom,Dad):
    def cash(self):
        print("Son's cash")
        super().cash()
        
s=Son()
s.cash()
'''
# multiple 
'''
class Dad():
    def cash(self):
        print("Dad's cash")
    
class Mom():
    def cash(self):
        print("Mom's cash")
        
class Son(Mom,Dad):
    def cash(self):
        print("Son's cash")
        super().cash()
        Dad().cash()
s=Son()
s.cash()
'''

#  multilevel 
'''
class Grand():
    def cash(self):
        print("Grandpa's cash")

class Dad(Grand):
    def cash(self):
        print("Dad's cash")
        super().cash()

class Son(Dad):
    def cash(self):
        print("Sons's cash")
        super().cash()

s=Son()
s.cash()
'''

# hierrchical
'''
class Dad():
    def cash(self):
        print("Dad's cash")

class Son(Dad):
    def cash(self):
        print("Sons's cash")
        super().cash()

class Daughter(Dad):
    def cash(self):
        print("daughter's cash")
        super().cash()
s=Son()
s.cash()

d=Daughter()
d.cash()
'''

# Hybrid
'''
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B")       
class C(A):
    def __init__(self):
        print("C")
class D(B):
    def __init__(self):
        super().__init__()
        print("D")
class E(C):
    def __init__(self):
        print("E")
class F(D,E):
    def __init__(self):
        super().__init__()
        print("F")
f=F()
'''
# op -- ABCDEF
'''
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        super().__init__()
        print("B")       
class C(B):
    def __init__(self):
        super().__init__()
        print("C")
class D(B):
    def __init__(self):
        super().__init__()
        print("D")
class E(D):
    def __init__(self):
        super().__init__()
        print("E")
class F(E,C):
    def __init__(self):
        super().__init__()
        print("F")
f=F()
'''


# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 31-03-2026

#
'''
class A:
    def __init__(self,name):
        print("Yo ",name)
class B:
    def __init__(self):
        print("B")
b=B()
'''


#
'''
class A:
    def __init__(self,name):
        print("yo ",name)
class B(A):
        pass
b=B("Zoro")
'''

#

'''
class A:
    def __init__(self,name):
        print("yo ",name)
class B(A):
    def __init__(self):
        super().__init__()
class C(B):
    def __init__(self):
        super().__init__("Zoro")
c=C()
'''

#

'''
class A:
    def __init__(self,name):
        print("yo ",name)
class B(A):
    def __init__(self):
        print("Yokoso")
class C(B):
    def __init__(self):
        A.__init__(self,"Zoro")
c=C()

'''

# polymorphism:

# poly -- many
## morphism -- forms

# +

'''
a=20
b=10

print(a+b)

a="sakasama"
b=" no sekai"

print(a+b)
'''

#Method OverLoading -- compile time polymorphism

# same class and same method name burt different paarameters.

## python doesn't support do importing multiple dispatch -- @dispatch

#__________________________________________________________

# Method Overriding -- runtime polymorphism

#different class same method name and same parameters.
## python supports this

# reference for method overloading
'''
class A:
    def func(self,a,b):
        print(a+b)
    def func(self,a,b,c=0):  # here it is the one running
        print(a+b+c)
a=A()
a.func(10,20)
'''

#
'''
class A:
    def func(self,*args):
        count=0
        for i in args:
            count=count+i
        print(count)
a=A()
a.func(10,20,30)
'''


# ____________________________________________________________________________________________________________________________________________________________________________________________

#             tuesday - leave                                        Date: 01-04-2026

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                     Date: 02-04-2026

# method overloading in another file in vs code



# Encpsulation

## public
'''
class A:
    def func(self,x):
        self.x=x
        print(self.x)
a=A()
a.func(10)
'''
# we can ccess in another class is public
'''
class A:
    def __init__(self,x):
        self.x=x
class B(A):
    def display(self):
        print(self.x)
b=B(7)                             # -- here only have to give argument
b.display()
'''
#
'''
class A:
    def func(self,x):
        self.x=x
a=A()
a.func(96)
print(a.x)              # we can access in outside also public
'''
# here we access inherits in another class and print is also public
'''
class A:
    def func(self):
        print("Yo")
class B(A):
    def display(self):
        self.func()
b=B()
b.display()
'''

# private can access only its own class not other class__ double underscore is the private declaration

##but can access in other class using calling the class name  --  name manging method

#
'''
class A:
    def func(self,x):
        self.__x=x
        print(self.__x)
a=A()
a.func(18)
'''
#
'''
class A:
    def __init__(self,x):
        self.__x=x
    def display(self):
        print(self.__x)
a=A(10)
a.display()
'''

# this is name manging
'''
class A:
    def __init__(self,x):
        self.__x=x
class B(A):
    def  display(self):
        print(self._A__x)       # here if (self.__x) is error cuz its private  
b=B(10)
b.display()
'''

# same name manging outside calling
'''
class A:
    def __init__(self,x):
        self.__x=x
class B(A):
    def display(self):
        print(self._A__x) # here self
b=B(10)
b.display()
print(b._A__x)  # here b
'''
# private method
'''
class A:
    def __func(self):
        print("yokoso")
class B(A):
    def display(self):
        self._A__func()  # name manging private method

b=B()
b.display()
b._B__func()
'''
#  summa 
'''
class __A:
    def func(self):
        print("sakasama no sekai")
class B(__A):
    def display(self):
        self.func()
b=B()
b.func()
'''

# protected: using --  _ single uderscore  -- naming conversion

# argument
'''
class A:
    def func(self,x):
        self._x=x
        print(self._x)
a=A()
a.func(10)
print(a._x)  # outside of the class argument
'''
# another method argument
'''
class A:
    def func(self,x):
        self._x=x
    def display(self):
        print(self._x)
a=A()
a.func(10)
a.display()
'''
# another class argument
'''
class A:
    def __init__(self,x):
        self._x=x
class B(A):
    def display(self):
        print(self._x)
b=B(10)
b.display()
'''
# method protected inside classs
'''
class A():
    def _func(self):
        print("Bankai")
    def display(self):
        self._func()
a=A()
a.display()
'''
# outside another class
'''
class A():
    def _func(self):
        print("Genjutsu")
class B(A):
    def display(self):
        self._func()
b=B()
b.display()
'''


# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                     Date: 03-04-2026

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                     Date: 04-04-2026

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                     Date: 05-04-2026


# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                     Date: 06-04-2026

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                     Date: 07-04-2026

