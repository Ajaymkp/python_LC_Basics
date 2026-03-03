#      Function                                                                  Date: 02-03-2026

#block of code can perform a specific task:
'''
def func_name():
    print("yo")
func_name()
func_name()              # code is reusable whenever we want
'''
 # function -- Eg:  name == parameter  and "Zoro" == Argument
'''
def func(name):
    print(f"Yo {name}")
func("Zoro")
func("Sanji")
'''
# function odd or even
'''
def odd_even(n):
    if n%2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

odd_even(5)
odd_even(6)
'''
# function inside get input
'''
def func(name):
    print(f"yo {name}")
n=input("Enter a name: ")
func(n)

m=input("Enter a name: ")
func(m)
'''
# ____________________________________________________________________________________________________________________________________________________________________________________________

                                   ### Types of Arguments

   # 1. Positional
   # 2. Keyword
   # 3. Default
   # 4. Arbitary Positional
   # 5. Arbitary Keyword
# ____________________________________________________________________________________________________________________________________________________________________________________________

# 1. Positional Argument:  -- {ordered format reading} -- {also all arguments}
'''
def pos_arg(name):
    print(f" yo {name}")
pos_arg("Sanji")
'''

'''
def pos_two(name,reg):
    print(f"yo {name} reg:{reg}")
#pos_two("luffy")                # -- TypeError: pos_two() missing 1 required positional argument: 'reg'
pos_two("zoro","hell")
pos_two("hell","zoro")           # -- here order changes 
'''
# 2. Keyword Argument:

'''
def key_arg(name,no):
    print(f" yo {name} no: {no}")
key_arg(name="Ace",no=2)
'''
 # keyword argument follows positional argument
'''
def key_two(name,title,fruit):
    print(f"{name} {title} {fruit}")

         # keyword argument follows positional argument
key_two("ace",title="2nd div captain",fruit="fire fire fruit")  # this works
'''
          # but positional argument does not follows keyword argument

#key_two(name="ace","2nd div captain","fire fire fruit")  # Syntax error

# 3. Default Argument:

 # -- default parameter doesn't follows without default parameter : -- syntax error
'''
 def def_arg(a=1,b):          # syntax error
    print(a+b)
def_arg(b=2)
'''

'''
def default_arg(a=0,b=1):
    print(a+b)
default_arg(10,5)
default_arg()          # -- here take default values what we give
'''



# 4. Arbitary positional Argument:       * -- means mulptiple positional arguments can read
                # -- tuple of arguments
'''
def arb_pos_arg(*args):
    print(sum(args))
arb_pos_arg(10)
arb_pos_arg(10,20)
arb_pos_arg(10,20,30)
arb_pos_arg(10,20,30,40,50,60,70)
'''
'''
def arb_pos_two(*args):
    s=0
    for i in args:
        s+=i
    print(s)
arb_pos_two(10,20,30,40,50,60)
'''

# 5. Arbitary Keword Argument:   ** -- means multiple kewword arguments can read
         # dictionary of arguments
'''         
def arb_key_arg(**kwargs):
    print(kwargs)
arb_key_arg(name=ace,no=2)
'''
'''
def arb_key_two(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
arb_key_two(name="ace",title="2nd div captain",fruit="fire fire fruit")

'''

 # ____________________________________________________________________________________________________________________________________________________________________________________________

#   Built-in functions:                                                        Date: 03-03-2026


##     abs    (absolute):
'''
a=-3
b=3
print(abs(a),abs(b))
'''
##    pow    (power):
'''
p=5
print(pow(p,2))
'''
##    sum    (addition):
'''
s=[10,20,30]
su=(10,20,30)
print(sum(s),sum(su))
'''
##    range  (range of int) :
'''
r=7
print(range(r))
'''

                 ##   min       (minimum num in group of nums):

m=[10,20,30,40,50]

##print(min(m))

                     ##   max     (maximum num in group of nums):

##print(max(m))

##  round    (round of a float into int):
'''
a=6.5
b=6.6
print(round(a),round(b))
'''
a=[False,False]
b=[True,False]
c=[False,True]
d=[True,True]

e=[1]
f=[0]

g=[""]
h=[" "]
i=[]
j=""
## any   -- OR GATE --   (any one True --op will True):
'''
print(any(a))
print(any(b))
print(any(c))
print(any(d))
print("----------------")
print(any(e))
print(any(f))
print("----------------")
print(any(g))
print(any(h))
print("----------------")
print(any(i))
print(any(j))
'''
## all     -- AND GATE -- (all every one have to be True for -- op True)
'''
print(all(a))
print(all(b))
print(all(c))
print(all(d))
print("----------------")
print(all(e))
print(all(f))
print("----------------")
print(all(g))
print(all(h))
print("----------------")
print(all(i))
print(all(j))
'''

## bin
'''
a=1
print(bin(a))
'''

## boolean
'''
m=0
n=1
o=""
p=" "
q=[]
r=[" "]
s=None

print(bool(m))
print(bool(n))
print(bool(o))
print(bool(p))
print(bool(q))
print(bool(r))
print(bool(s))
'''

## enumerate()
'''
e=['ace','sabo','luffy']
for i,j in enumerate(e):
    print(i,j)

for i,j in enumerate(e,7):                # --- where will start
    print(i,j)
'''
## zip()
'''
a=[10,20,30]
b=[30,40,50]
d=[1,2,3,4]
c=zip(a,b)
print(list(c))

e=zip(a,d)
print(list(e))
'''
## unzip  ---  a.b =zip(*x)
'''
f=[(10, 30), (20, 40), (30, 50)]
g,h=zip(*f)
print(g,h)
'''
##i=dict [g] [h]
##print(i)

## shallow copy

    #   1.  shallow copy creates a new outer object
    #  but references the same nested mutable objects.

    # 2. if nested mutable objects mutated . it will affect original.
  
import copy
'''
a=[1,2,3,4]
b=copy.copy(a)   
print(a,id(a))
print(b,id(b))
'''

'''
c=[[1,2],[3,4],5]
d=copy.copy(c)

print(c,id(c))
print(d,id(d))
d.append(6)             # it doesn't affects c
d[0].append(0)        ###### --- it does affects c ---
print(c,id(c))
print(d,id(d))      
'''

## deep copy


    #   1. deep copy recursively copies all nested objects
    #  creating independent memory allegations.


'''
a=[1,2,3,4]
b=copy.deepcopy(a)   
print(a,id(a))
print(b,id(b))
'''

'''
c=[[1,2],[3,4],5]
d=copy.deepcopy(c)

print(c,id(c))
print(d,id(d))
d.append(6)             # it doesn't affects c
d[0].append(0)        # it doesn't affects c
print(c,id(c))
print(d,id(d))      
'''

## return              ----    (Back to the caller Doesn't read any after funtion code)



def return_2():
    return "Ace"          # -- exit here
    return "sabo"          # -- doesn't read here   
print(return_2())


def return_2():
    return "Ace"          # -- exit here
    print("sabo")         # -- doesn't read here   
print(return_2())

def return_2():
    print("Ace" )         # -- exit here
    return "sabo"          # -- does read here   
print(return_2())







 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 04-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 05-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 06-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 07-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 08-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 09-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                        Date: 10-03-2026



 # ____________________________________________________________________________________________________________________________________________________________________________________________
