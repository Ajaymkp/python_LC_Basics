      ###  DATA STRUCTURES

          # LIST
          # TUPLE
          # SET
          # DICTIONARY





#       List         is mutable means add any data type inside                                                                       Date: 19-02-2026

 ### .append()

a=[10,20,30,40]
b=50
'''
c="ace".upper()

a.append(b)
a.append(60)
print(a)

a.append(c)
print(a)
'''
         ### .index()
'''
n=[10,20,30]
##m=n.index(20)
print(m)
print(n.index(30))


a=[10,20,[30,40,[50,60,70,80],92,[12,23,34,[45,56,67,[78,89,90,98],87,76,65],54],43],32,21]   # cant find using .index() cause nested index
print(a[2][4][3][3][2])
b=[10,20,[30,[40,50,60,[70,80,90],25,[35,45,55]],65,75],85]              # interview question
print(b[2][1][5][1])
'''

 ## .extend([])
'''
a=[10,20,30,40,50,60]
#a.extend(80)                  ## can't cuz of it is int if int iside of list only valid (not only int any data type insideof list valid)
a.extend([70])                ## like this
a.extend(['a','c','e'])        ## like this also

a.extend("luffy")         ## it will also add but separate every sinle letters with different index
a.extend(["sanji"])

print(a)
'''
    ### .insert  ()
'''
a=[10,20,30]
a.insert(1,15)  # insert in the index what we give
a.insert(4,[40,50,60])

print(a)
'''

 ### replace
'''
b=[10,20,30,40]
b[2] = 50
print(b)
'''

   ### .sort()

s=[10,60,30,70,50,30]
'''
s.sort()
print(s)

print(s.sort())
'''
  ### .count()
'''
c=s.count(30)       # how many elements in the list
print(c)
print(s.count(30))
'''

  ## .remove()   based on values
'''
s.remove(50)

print(s)
'''
  ### .pop()      # based on index
'''
s.pop()               # It will pop last index value
print(s)
s.pop(1)
print(s)
'''
  ### delete     # del x[:]
'''
d=[1,2,3,4,5]
del d[0:2]             # based on index also but we can give start and end
print(d)

'''

  ## .reverse()
'''
r=[10,20,30,40,50]
r.reverse()
print(r)
'''
  ## .copy()
'''
c=[10,20,30,40]
d=c.copy()
print(d)

c.append([40])
print(c)
print(d)
'''

  ## .clear()
'''
c=[20,40,60]
####  c.clear(40)             # error -- cause it takes no argument
c.clear()               # clear all values
print(c)
'''

#____________________________________________________________________________________________________________________________________________________________________________________________


##     List                                Tuple

#       mutable                          immutable
#       dynamic memory          fixed memory
#       many methods               few methods
#       slow                              fast because immutable
#       inefficient memory        efficient memory

#____________________________________________________________________________________________________________________________________________________________________________________________
#       ### Tuple                                                                                  Date: 20-02-2026

  # IMMUTABLE
  # CAN STORE ANY DATA TYPE
  # FIXED AND LESS MEMORY
  # FASTER THAN LIST
  # ALLOW DUPLICATE VALUES
  # ORDERED
  # ()                              using symbol
                  ### store any data type
'''
a = (10,20,30,40)
print(a)
print(type(a))

a=(10,"apple",4.5,"bananaa")
print(a)
'''
# Allow Duplicate value
'''
a=(10,20,10)
print(a)
'''
# index
'''
a=(10,20,30,40,50)
print(a[0])
print(a[1])
print(a[5])
'''
# index     # nested Tuple
'''
a=([10,20],50)
print(a[0][1])
'''
#   .count()
'''
b=a.count(10)
print(b)
'''
# concat
'''
a=(1,2,3)
b=(4,5,6)
print(a+b)
print(b+a)
print(a)
print(b)
'''
#                                      Tuple TC to List .append() method and back to TC Tuple
'''
a=(1,2,3,4,5,6)
b=5
c=list(a)
c.append(b)
c.append(8)
print(a)
print(c)
print(tuple(c))
'''


  ## type :
'''
i=(18)                     # int not tuple
s=("Ace")               # string not tuple
t=(18,"Ace")           # tuple
print(i, s, t)
print(type(i), type(s), type(t))
'''

  ## tuple inside tuple
'''
t=(1,2,3,(5,6,7),8,9)
print(t)
print(type(t))
print(t[3][2])
'''


 ### SET

# mutable
# do not allow duplicate
# only store {immutable} data type only
# unordred
# cant access index
# {}                                                               -- using symbol as like as maths Set


'''
a={10,20,30,40}                    # here can't
small={1,3,2,4,6,5}                    # if range is low it can order it (sort)
print(a)                                      # it will print randomly order
print(small)
'''

#print(a[0])    ----   error 

a={"apple","orange", "mango", "banana"}
#print(a[0])     -- there is no indexing

#  don't allow duplicate values
'''
a={1,2,1,2}
print(a)

# list inside set 
b={1,2,3,[4,1,2],6}         # unhashable type: 'list'   -- error
#print(b)
'''

# tuple iside set
'''
c={1,2,3,(1,2),6}         ### TUPLE is allowed inside of set , cuz TUPLE is IMMUTABLE
print(c)
'''
# SET INSIDE SET
'''
##d = {1,2,3,{4,5,6},7}             ###  (unhashable type: 'set')
##print(d)
'''

# .update()
'''
a={1,2,3}
b={4,5,10}

b.update(a)          ####   this will add a in b and change b a+b    -- with order

print(a)
print(b)
'''

  ### .remove()            
'''
r={1,2,3,4,5}
r.remove(4)                 # it works cuz it is based on values
print(r)                        # but del and pop() are based on index so these are not works
'''
##r.remove(6)               #  error -- cuz it is not there
##print(r)

  ### .discard()
'''
d={1,2,3,4,5}
d.discard(4)
print(d)

d.discard(6)                    # doesn't throw error this is the difference between remove
print(d)
'''
  ## .clear()
'''
a={1,2,3,4}
a.clear()
print(a)                      # clear all values in set so print ---- set{}
'''
  ### .pop()

'''
p={10,20,30,40,50,60}
p.pop()                    # this only works cuz is not indicating index
#p.pop(00              # It will throw -- error
print(p)
'''
#____________________________________________________________________________________________________________________________________________________________________________________________



  ###    Venn diagram -- Sets


a={1,2,3,4}
b={3,4,5,6}

# .union()         # | -- union symbol
'''
c=a.union(b)         # 1. st method
print(c)
print(a|b)             # 2. nd method
'''
# .intersection()      # & == Ampersand
'''
d = a.intersection(b)  # 1. st method
print(d)        
print(a&b)   # 2. nd method
'''
# .difference()    #     -      --  minus symbol
'''
e = a.difference(b)   # 1. st method
print(e)
print(a-b)              # 2. nd method

print(b-a)
'''
# .symmetric_difference()
'''
f=a.symmetric_difference(b)
g=b.symmetric_difference(a)
print(f)
print(a^b)
print(b^a)
'''  
#____________________________________________________________________________________________________________________________________________________________________________________________
#       ASSESSMENT --                                                                                 Date: 21-02-2026


#____________________________________________________________________________________________________________________________________________________________________________________________
#         SUNDAY -- HOLIDAY                                                                              Date: 22-02-2026







#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 23-02-2026

   ### DICTIONARY -- {}

# Mutable
# Key value pair
# Value can allow duplicate
# But key can't allow duplicate
# Value can allow allow mutable datatype
# key allow immutable datatype only  {NOT MUTABLE DATA}
# ordered

#____________________________________________________________________________________________________________________________________________________________________________________________
'''      
a={1:'ace','a':'sabo','joyboy':'luffy',"Monkey D":"Dragon"}
print(a,type(a))
'''
# duplicate testing in both key:value
'''
dv={1:'ace',2:'sabo',3:'ace'}      # Here no problem
dk={1:'ace',2:'sabo',1:'luffy'}    # {1: 'luffy', 2: 'sabo'} -- reads last dup key only

print(dv , dk)
'''
# ordered             ##  how we give == op --- not like set 
'''
o={3:'ace',1:'sabo',2:'ace'} 
print(o)
'''
# Mutable data testing in both key:value

'''
mv={1:100,'a':'sabo','ace':[10,20],4:(5,10),5:{15,30},6:{1:'zoro'}} 
im={(1,2):99}   # -- cuz this is imutable
#mk={[1,2]:'sanji',{3,4}:'tony',{1:'zoro'}:'tony'}  #-- TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
print(mv , im)
'''


# key index
'''
a={3:'ace',1:'sabo',2:'luffy'}
print(a)
print(a[3])
'''

#.get()


b={'a':'zoro','b':'sanji','c':'luffy'}
#print(b.get('c'),b.get('d'),b.get('e',7))


# add
'''
a={3:'ace',1:'sabo',2:'luffy'}
a[4]='zoro'
print(a)
'''

# .()update
'''
a={1:'ace',2:'sabo',3:'luffy'}
b={'a':'zoro','b':'sanji','c':'luffy'}
a.update(b)
print(a)
b.update(a)
print(b)
'''
# x.keys()
'''
k={1:'ace',2:'sabo',3:'luffy'}
b={'a':'zor0','b':'sanji','c':'luffy'}
print(k.keys() , b.keys())
'''
# .values()
'''
v={1:'ace',2:'sabo',3:'luffy'}
print(v.values())
'''
# .items()
'''
a={1:'ace',2:'sabo',3:'luffy'}
print(a.items())
'''
# .clear()
'''
a={1:'ace',2:'sabo',3:'luffy'}
print(a.clear())
'''
# .pop()  and .popitem()
'''
a={1:'ace',2:'sabo',3:'luffy'}

#a.pop()                                              -- error   cuz need 1 arguement 

a.popitem()
print(a)
'''
# delete  -- del x[] = ''
'''
b={'a':'zoro','b':'sanji','c':'luffy'}
del b['b']
print(b)
'''
# .setdefault()      -- c and d  is affecting b

b={'a':'zoro','b':'sanji','c':'luffy'}
c=b.setdefault('d')                                             # OP:  -- None
d=b.setdefault('e','nami')                                # OP:  -- nami
#print(b,c,d)

#____________________________________________________________________________________________________________________________________________________________________________________________
            

# For loop in List                     ~

a=[1,2,3]
b=[4,5,6,7]

#print(a+b)                              ~

'''
for i in range(len(b)):
    a.append(b[i])
print(a)
'''
# remove values in List without method 

r=[10,20,30,40]
s=40
c=list([])
#r.remove(50)
#print(r)
'''
for i in range(len(r)):
    if s == r[i]:
        continue
    else:
        c.append(r[i])
print(c)
'''
# rev

'''
for i in range(len(r)-1,-1,-1):
        c.append(r[i])
print(c)
'''




#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 24-02-2026

# REV -- Another method
'''
for i in range(len(r)):
    for j in range(i,len(r)):
        r[i], r[j] = r[j], r[i]
print(r)
'''
# Sort -- without using method

'''
s=[20,40,30,10]
#s=[5,6,4,2]
for i in range(len(s)):
    for j in range(i,len(s)):
     #   if s[i] < s[j]:                                    # OP-- [40, 30, 20, 10]
        if s[i] > s[j]:                                     # OP-- [10, 20, 30, 40]
            s[i],s[j] = s[j],s[i]
    print(s)
'''
# add two lists:

l=[[1,2,3,],[10,20,30]]
k=[]
'''
for i in l:
    k.extend(i)
print(k)
'''
# Another method:
m=[]
'''
for i in l:
    for j in i:
        m.append(j)
    print(m)
'''

#vowels print in list:

'''
a="sanji"
b=[]
for i in a:
    if i in "aeiou":
        b.append(i)
print(b)
'''
#   op :  --  [[1, 4], [2, 5], [3, 6]]
'''
a=[[1,2,3],[4,5,6]]
b=[]

for i in range(len(a[0])):
        b.append([a[0][i],a[1][i]])
print(b)
'''
# op: -- [[1,2,3],[4,5,6]]

'''
b=[[1, 4], [2, 5], [3, 6]]
c=[]
for j in range(len(b[0])):
    c.append([b[0][j],b[1][j],b[2][j]])
print(c)
'''
# Remove Duplicate values:
s=[1,2,3,4,5,6,2,3]
t=[]
'''
for i in s:
        if i not in t:
            t.append(i)
print(t)
'''
# maximum without builtin methods:

m=[2,4,6,34,75,98,12]
n=a[0]
'''
for i in m:
    if i>n:             # -- Maximum number
        n=i
print(n)
'''
'''
for i in m:
    if i<n:                      # -- Smallest number
        n=i
print(n)
'''

#### -------    Communnication skills in CS file.txt                                     -------------




## Assessment  ---  Second Largest Number
'''
a=[10,50,20,30,40]
b=0
c=0
for i in a:
    if i>b:
        b=i
print(b, "is the maximum value")
for i in a:
    if i>c and i<b:
        c=i
print(c, "is the second max value")
'''











#____________________________________________________________________________________________________________________________________________________________________________________________
# Second Largest Number                                                                          Date: 25-02-2026

a=[10,42,23,34,25]
l=a[0]
s=a[1]
'''
for i in range (len(a)):
    if l<a[i]:
        s=l
        l=a[i]
    elif s<a[i] and l!=a[i]:
        s=a[i]
print(s)       
'''
## Anangram
'''
a="heart"
b="earth"

print(sorted(a))
print(sorted(b))

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anangram")
'''

##  if a= [0,1,2,0,3]                      op: -- [1,2,3,0,0]
a=[0,1,2,0,3]
b=[]
c=[]
'''
for i in range(len(a)):
    if a[i] != 0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b+c)
'''
'''
for i in a:
    if i != 0:
        b.append(i)
    else:
        c.append(i)
print(b+c)
'''

x=0               # --- Another Method
'''
for i in range(len(a)):
    if a[i]!=0:
        a[i],a[x]=a[x],a[i]
        x+=1
print(a)
'''

a=[0,2,3,4,6,7,11,9,5]            # --- op:[2,7]  two pointer mens l and r
a.sort()
b=9
'''
l=0
r=len(a)-1
while l<r:
    x=a[l]+a[r]
    if x==b:
        print([a[l],a[r]])
        l+=1
        #break
    elif x<b:
        l+=1
    else:
        r-=1
'''
a=[1,2,3,4]
b=[3,4,5,6,7]
c=[]
'''
for i in a:
    for j in b:
        if i==j and i!=c:
            c.append(i)
print(c)
'''
'''
for i in a:
    if i in b:
        c.append(i)
print(c)
'''
      #  0p: --- {1,2,3,4,5,6} union
'''             
a={1,2,3}
b={4,5,6}
c={}
for i in a:
    b.add(i)
print(b)       
'''
 # intersection

a={1,2,3}   
b={3,4,5}
'''
c=set()
for i in a:
    if i in b:
        c.add(i)
print(c)
'''
# difference
'''
for i in b:
    if i in a:
        a.remove(i)      
print(a)
'''
#symmetric_difference 
'''
c=set()

for i in a:
    if i  not in b:
        c.add(i)
for i in b:
    if i not in a:
        c.add(i)
print(c)
'''

  # isdisjoint()
'''
a={1,2,3}
b={4,5,6}

print(a.isdisjoint(b))
print(b.isdisjoint(a))
'''





#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 26-02-2026

#Dictionary   ----  op; {1:1, 2:4, 3:27. 4:256}
'''
a=[1,2,3,4]
b={}
c=0

for i in a:
    c=i**i
    b[i]=c
print(b)
'''
#       op:        -- {'apple': 5, 'orange': 6, 'mango': 5, 'banana': 6}
'''
a=['apple', 'orange','mango','banana']
b={}
for i in a:
    b[i]=len(i)
print(b)
'''

# Op: -- {'b': 1, 'l': 2, 'a': 2, 'c': 1, 'k': 1, ' ': 2, 'e': 1, 'g': 1, 's': 1, 'n': 1, 'j': 1, 'i': 1}

a="black leg sanji"
x={}

'''
count=0
for i in a:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print(x)
'''
     ### another method but have duplicate keys --- but it works in dictionary
count=0
'''
for i in a:
    x[i]=a.count(i)
print(x)
'''        
#  op:  -- {1:'a', 2:'b',3:'c', 4:'d'}
a={'a':1, 'b':2,'c':3,'d':4}
b={}
x=1
##c=a.keys()
##print(c)
'''
for i in a:
    b[x]=i
    x+=1
print(b)
'''
# another metjod
'''
for i in a.keys():
    for j in a.values():
        b[j]=i
        print(b)
'''
# another method
'''
for i ,j in a.items():
    b[j]=i
print(b)
'''
 ### y.update(x) with out built-in methods.     --  {.union() }

x={1:'a', 2:'b',3:'c', 4:'d'}
y={5:'e', 6:'f',7:'g', 8:'h'}
'''
for i,j in y.items():
    x[i]=j
print(x)
'''
# .intersction() with out built-in methods.

x={'a':1,'b':2,'c':3,'d':4}
y={'c':6,'d':4,'e':5}
z={}
'''
for i,j in x.items():
    for k,l in y.items():
        if i==k and j==l:
            z[i]=j
print(z)
'''
                             ##### Important for key and value   i in y === key
'''
for i,j in x.items():
    if i in y and y[i]==j:                ## -- y[i]==j
            z[i]=j
print(z)
 '''   
# a.difference(b) with out built-in methods.

a={'a':1,'b':2,'c':3}
b={'c':3,'d':4,'e':5}
'''
for i,j in b.items():
    if i in a and b[i]==j:
        del a [i]
print(a)
'''
#b.differnce(a)
for i,j in a.items():
    if i in b and a[i]==j:
        del b [i]
print(b)

#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 27-02-2026


#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 28-02-2026


































