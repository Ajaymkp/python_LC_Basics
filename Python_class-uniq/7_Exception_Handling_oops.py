#     Exception Handling                                          Date: 16-03-2026

# Its allow to gracefully handleruntime error
# in the python program without crashing program.

## only one try block but multiple except block.

### try block lets you to test a code for errors.

#### except block let you to handle error.

##### finally block lets you execute code
##### regardless of the result of the try and except.


'''
a=5
b=0
#print(a/b)
print("Yo")       #  If error occurs IT will not run
'''

# try
'''
try:
    a=int(input())
    b=int(input())
    print(a/b)
except:
    print("error")
'''

# Zero error
'''
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("error")
'''
# try -- ZeroDivisionError  -- Specified the Zeroerror only
'''
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError as z:
    print(z)
'''

# ZeroDivisionError and ValueError -- both are specified
'''
try:
    a=int(input())
    b=int(input())
    print(a/b)
except  ZeroDivisionError as z:
    print(f"ZeroDivisionError: {z}")
except ValueError as v:
    print(f"ValueError: {v}")

'''

#else     -- If no error in try , It will run

'''
try:
    a=int(input())
    b=int(input())
    print(a/b)
except  ZeroDivisionError as z:
    print(f"ZeroDivisionError: {z}")
except ValueError as v:
    print(f"ValueError: {v}")
else:
    print("No Error")
'''

#  finally -- always run

'''
try:
    a=int(input())
    b=int(input())
    print(a/b)
except  ZeroDivisionError as z:
    print(f"ZeroDivisionError: {z}")
except ValueError as v:
    print(f"ValueError: {v}")
else:
    print("No Error")
finally:
    print("See you")
'''

#
'''
num = [1,2,3,6,7,8]
a=9
l=0
add = 0
r=len(num)-1
while l < r:
    add = num[l]+num[r]
    if add == a:
        print([num[l],num[r]])
        l+=1
    elif add < a:
        l+=1
    else:
        r-=1
'''
# op: -- e5d4c3b2a1
'''
a="abbcccddddeeeee"
x={}

count=0
for i in a:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
y=[]
for i,j in x.items():
    y.append((i,j))
print(y)

z=sorted (y, key=lambda x:x, reverse=True)
print(z)

res =""
for m,n in z:
    res+=m+str(n)
print(res)

'''

# 2'nd most frequent digit
'''
a=[5,4,4,6,6,6]
b={}

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)

c=[]
for i,j in b.items():
    c.append((i,j))
print(c)

d=sorted (c, key=lambda x:x[1], reverse=True)
print(d)
print(d[1][0])
'''
#  op == [24,12,8,6]

# all multiple
# and divide by input by increacing 1 index
'''
x=[1,2,3,4]
m=1
n=0
y=[]
for i in x:
    m*=i
for i in x:
    n=m//i
    y.append(n)
print(y)

'''

# False

##print(0.1+0.2==0.3)


# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 17-03-2026
# op -- [3,4,5,1,2]  -- change upto input  index 
'''
x=[1,2,3,4,5]
y=2
z=x[y:]+x[:y]
print(z)
'''
# Alternate change upto input index to last
'''
a=[1,2,3,4,5]
b=int(input())

for i in range(b):
    x=a.pop(0)
    a.append(x)
print(a)
'''
# Alternate

'''
a=[1,2,3,4,5]
b=int(input())
for i in range(len(a)-1):
    if i <= a.index(b+1):
        x=a.pop(0)
        a.append(x)
        print(a)
'''

##      non repeating string to print here -- b
        

# Another Method
'''
x="aabccc"
def func(a):
    for i in a:
        if a.count(i)==1:
            return i
print(func(x))
'''
# Another Method it s not fully complete

'''
a="aabcc"
for i in a:
    if a.count(i)==1:
         print(i)
'''
#  Missing Sequence Numbers -- op -- [4,6]

'''
x=[1,2,3,5,7]
y=[]
z=x[0]
for i in range(len(x)):
    if x[i] != z:
        y.append(z)
    z=x[i]+1
print(y)
'''

# longest substring  -- Works but not for all
'''
a="ababcbaac"
#a="bankaitensazangetsu"
##b=list(a)

x={1:""}
j=1
for i in a:
    if i not in x[j]:
        x[j]+=i
    else:
        j+=1
        x[j]=i
print(x)

##print(x.values())
##m={1:"abc",2:"ab"}
##print(m[2])

y=[]
for i in x.values():
    if len(i)>len(y):
        y=i
print(y)
'''


### ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 18-03-2026
#longest substring without duplicate values
'''
##x="bankaitensazangatsu"
x="abadbc"
s=set()
l=0
length=0

for r in range(len(x)):
    while x[r] in s:
        s.remove(x[l])
        l+=1
    s.add(x[r])
    length=max(length,r-l+1)
print(length)
'''          

 ##    if length>r-l+1:
##        length = length
##    else:
##        length = r-l+1

# op -- ["cba","fed"] -- reverse string inside list
'''
x=["abc","def"]
y=[]
z=""
for i in x:
    for j in i:
        z=j+z
    y.append(z)
    z=""
print(y)
'''

# Duplicate times diferent Values 
'''
a=[1,2,2,1,3,1,3]
b={}
c=0
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
print(b)
d=set(b.values())
e=list(b)
if len(d)== len(e):
    print("True")
else:
    print("False")
'''
# Same Method but simple for loop
'''
a=[1,2,2,1,3,1,3]
b={}
c=0
for i in a:
    b[i]=a.count(i)

print(b)
d=set(b.values())
e=list(b)
if len(d)== len(e):
    print("True")
else:
    print("False")
'''

# op -- "abcdabef" removal of sequence of non repeating strings



'''
a="aaabcddabbef"
b=""
for i in range(len(a)):
    if a[i] != a[i-1]:
        b+=a[i]
print(b)
'''
# Slightly differnece


'''
a="aaabcddabbef"
b=""
s=a[0]
for i in range(1,len(a)):
    if a[i] != a[i-1]:
        s+=a[i]
print(b)
'''

# op -- [[1,1,1],[2,2],[3,3,3],[4,4]]
'''
x=[1,1,2,4,2,3,1,3,3,4,4]
x.sort()
print(x)
y=[]
z=[x[0]]
for i in range(1,len(x)):
    
    if  x[i] == x[i-1]:
        z.append(x[i])
    else:
        y.append(z)
        z=[x[i]]
y.append(z)
print(y)
'''
# op -- [[1,1,1],[4,4],[2,2],[7],[6],[5]]

'''
x=[1,1,1,2,2,4,4,5,6,7,8]
y=[]
z=[x[0]]
for i in range(1,len(x)):
    
    if  x[i] == x[i-1]:
        z.append(x[i])
    else:
        y.append(z)
        z=[x[i]]
y.append(z)
print(y)

for i in range(len(y)):
    for j in range(i+1,len(y)):
        if len(y[i])<=len(y[j]) and y[i][0]<=y[j][0]:
            y[i],y[j]=y[j],y[i]
print(y)
'''        
# Another method
'''
a=sorted(y,key=lambda b:(len(b),b[0]) ,reverse=True)
print(a)
'''



# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 19-03-2026
d=[{"name":"urahara","age":23},{"name":"ichigo","age":24},{"name":"aizen","age":22}]
'''
# reverse sort by age

e=sorted(d,key=lambda x:x["age"],reverse=True)
print(e)

# sort by age 

f=sorted(d,key=lambda x:x["age"])
print(f)
'''

# 2 palindrome so true 

##op = True
##a="ababa"
##op = False


'''
a="noonmadam"
def palin(a):
    for i in range(1,len(a)):
        l=a[:i]
        r=a[i:]
        if l==l[::-1] and r==r[::-1]:
            return True
    return False
print(palin(a))
'''



# Another Method

'''
##a="noonmadam"
a="evevenoon"              ## ---   it is wrong
b=a[0]
c=""
d=""
e=""


for i in range(1,len(a)):
    if a[i] ==  a[0]:
        b+=a[i]
        break
    else:
        b+=a[i]
print(b)

for j in range(len(b),len(a)):
    c+=a[j]
print(c)

for i in b:
    e=i+e
print(e)

for j in c:
    d=j+d
print(d)

if b == e and c == d:
    print("True")
else:
    print("false")
'''

# op -- [1,2,3,4,5,6]
'''
x=[[1,3,5],[2,4,6]]
y=[]
for i in range(len(x[0])):
    y.append(x[0][i])
    y.append(x[1][i])
print(y)
'''

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 20-03-2026

# op -- 2,12,20,21,22,2 - total how many numbers have 2 , 1 upto 100

'''
n=int(input("n : "))
for i in range(1,n+1):
    if "2" in str(i):
        print(i)
'''        
# Move zeros to last op -- [1,2,3,4,0,0]
'''
a=[1,0,2,0,3,4]
b=[]
c=[]
for i in a:
    if i != 0:
        b.append(i)
    else:
        c.append(i)
b=b+c
print(b)
'''
# Another method
'''
a=[1,0,2,0,3,4]
b=[]
c=a.count(0)
for i in a:
    if i != 0:
        b.append(i)
b.extend([0]*c)
print(b)
'''

# Highest value to print -- op 45
'''
a={"a":12,"b":45,"c":23}
b=list(a.values())
m=b[0]
for i in b:
    if i > m:
        m=i
print(m)
'''
# Another Method
'''
a={"a":12,"b":45,"c":23}
m=max(a,key=a.get)
print(m)
'''
# longest common prefix"
'''
a=["flower","flow","flight"]
p=a[0]
for i in a[1:]:
    while not i.startswith(p):
        p=p[:-1]
print(p)
'''

# ouput valid if all are closed , if not Invalid 
'''
a=["(","[","]",")","("]

if "(" in a and ")" not in a :
    print("False")
elif "[" in   a and  "]" not in a:
    print("False")
elif "{" in  a and "}" not in a:
    print("False")
else:
    print("True")
'''
# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 21-03-2026

# Saturday -- Holiday -- Ramadhan

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 22-03-2026

# Sunday -- Holiday

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 23-03-2026

# Mukil Sir -- absent -- Assesment

# 1. arr=[2,1,8,7,6,3,10,9]   -- tar = 10  -- Two and Three sum
'''
a=[2,1,8,7,6,3,10,9]
a.sort()
b=[]
c=[]

target=10
l=0
r=len(a)-1

while l<r:
    s=a[l]+a[r]
    if s==target:
        b.append((a[l],a[r]))
        c.append((l,r))
        l+=1
    elif s>target:
        r-=1
    else:
        l+=1
print(a)
print(b)
print(c)
''' 
# Three sum
'''
a=[1,4,5,8,7,2]
a.sort()
b=[]
c=[]

t=10
l=0
r=len(a)-1
m=1
while l<r:
    s=a[l]+a[m]+a[r]
    if s==t:
        b.append((a[l],a[m],a[r]))
        c.append((l,m,r))
        l+=1
        m+=1
    elif s>t:
        r-=1
    else:
        l+=1
        m+=1
print(a)
print(b)
print(c)
'''
# 2. second Largest

'''
a=[10,20,30,45]
b=a[0]
c=a[1]

for i in a:
    if i > b:
        b=i
for i in a:
    if i > c and i != b:
        c=i
print(b," is the Largest Num")
print(c," is the Second Largest Num")
'''

# 3. count char in a string
'''
a="Bankai getsuha tenso".lower().replace(" ","")
b={}
for i in a:
    b [i] = a.count(i)
print(b)
'''

#4. Longest substring
'''
a="abacacabd"
b=0
c=0
d=set() 
for i in range(len(a)):
    while a[i] in d:
        d.remove(a[b])
        b+=1
    d.add(a[i])
    c=max(c,i-b+1)
print(c)
'''
# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 24-03-2026
# -- file handling --
# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 25-03-2026
# -- file hndling --
# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 26-03-2026
# -- half time -- file handling

# ____________________________________________________________________________________________________________________________________________________________________________________________

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

#                                                      Date: 29-03-2026

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

#                                                      Date: 29-03-2026

# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 29-03-2026
