#                -- Interview Questions ---                                                   Date: 24-02-2026

# REV -- Another method
'''
r=["l","u","f","f","y"]
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

##m=[2,4,6,34,75,98,12]
##n=a[0]
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
a=[0,1,2,0,3]
x=0               # --- Another Method
'''
for i in range(len(a)):
    if a[i]!=0:
        a[i],a[x]=a[x]i
print(a)
'''
# which two numbers addition gives 9
a=[0,2,3,4,6,7,11,9,5]            # --- op:[2,7]  two pointer means l and r
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
# Intersection
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
# Alternate method in single loop: time less
'''
for i in a:
    if i in b:
        c.append(i)
print(c)
'''

#---------------------------------------------------------------------------
# Set Methods without built-in methods

      #  0p: --- {1,2,3,4,5,6} union
'''             
a={1,2,3}
b={4,5,6}
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
'''
a={1,2,3}
b={3,4,5,6}
for i in b:
    if i in a:
        a.remove(i)
print(a)
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

##a={'a':1,'b':2,'c':3}
##b={'c':3,'d':4,'e':5}
'''
for i,j in b.items():
    if i in a and b[i]==j:
        del a [i]
print(a)
'''
#b.differnce(a)
'''
for i,j in a.items():
    if i in b and a[i]==j:
        del b [i]
print(b)
'''
#a.symmetric-difference()

##a={'a':1,'b':2,'c':3}
##b={'c':3,'d':4,'e':5}
##
##for i,j in b:
##    if 

#____________________________________________________________________________________________________________________________________________________________________________________________
#      ## List comprehension                                               Date: 27-02-2026

  

##a=int(input())
##b=[]

# normal way
'''
for i in range(1,a+1):
    b.append(i)
print(b)
'''
# sinle line
'''
c=[i for i in range(1,a+1) ]
print(c)
'''
# normal way of even numbers print:
'''
for i in range(1, a+1):
    if i % 2 == 0:
        b.append(i)
print(b)
'''
# single line even numbers using if andfor
'''
d=[i for i in range(1,a+1) if i%2 == 0]
print(d)
'''
# normal way of odd or even

'''
e=[]
for i in range(1,a+1):
    if i%2==0:
        e.append(f"{i} even")
    else:
        e.append(f"{i} odd")
print(e)
'''

# sinle line odd or even  using if,elsecand for

##f=[f" {i} even" if i%2 == 0 else f" {i} odd" for i in range(1,a+1)]
##print(f)

#____________________________________________________________________________________________________________________________________________________________________________________________


## Nested for loop and if condition:

# check divisible by 3 and 5:

##a=int(input())
##b=[]

'''
for i in range(1,a+1):
    if i%3 == 0:
        if i%5 == 0:
            b.append(i)
print(b)
'''
# single line
'''
c=[i for i in range(1,a+1) if i%3 == 0 if i%5 == 0]
print(c)
'''
# nested list add

x=[[10,20,30],[40,50,60]]
y=[]
'''
for i in x:
    for j in i:
        y.append(j)
print(y)
'''
# single line
'''
z=[j for i in x for j in i]
print(z)
'''
# Duplicate value remove:

x=[10,20,10,30,20]
y=[]

#       can't use in single line
'''
for i in x:
        if i not in y:
            y.append(i)
print(y)
'''
'''
for i in range(len(x)):
        if x[0:i+1].count(x[i])==1:
            y.append(x[i])
print(y)
'''
# single line:

##z=[x[i] for i in range(len(x)) if x[0:i+1].count(x[i])==1]
##print(z)

#____________________________________________________________________________________________________________________________________________________________________________________________

 ### Set Comprehension:  

##a=int(input())
##b=set()

# normal way
'''
for i in range(1,a+1):
    b.add(i)
print(b)
'''
# sinle line
'''
c={i for i in range(1,a+1) }
print(c)
'''
# normal way of even numbers print:
'''
for i in range(1, a+1):
    if i % 2 == 0:
        b.add(i)
print(b)
'''
# single line even numbers using if andfor
'''
d={i for i in range(1,a+1) if i%2 == 0}
print(d)
'''
# normal way of odd or even

'''
e=set()
for i in range(1,a+1):
    if i%2==0:
        e.add(f"{i} even")
    else:
        e.add(f"{i} odd")
print(e)
'''

# sinle line odd or even  using if,elsecand for

##f={f" {i} even" if i%2 == 0 else f" {i} odd" for i in range(1,a+1)}
##print(f)

#____________________________________________________________________________________________________________________________________________________________________________________________

## Nested for loop and if condition:

# check divisible by 3 and 5:

##a=int(input())
##b=set()

'''
for i in range(a):
    if i%3 == 0:
        if i%5 == 0:
            b.add(i)
print(b)
'''
# single line
'''
c={i for i in range(a) if i%3 == 0 if i%5 == 0}
print(c)
'''
# nested list add

x={10,20,30},{40,50,60}
y=set()
'''
for i in x:
    for j in i:
        y.add(j)
print(y)
'''
# single line
'''
z={j for i in x for j in i}
print(z)
'''
#____________________________________________________________________________________________________________________________________________________________________________________________

 ### Dictionary Comprehension:

##a=int(input())
##b={}

# int power of 2
'''
for i in range(1,a+1):
    b[i]=i**2
print(b)
'''
# singleline
'''
c={i:i**2 for i in range(1,a+1)}
print(c)
'''
# int power of 2 if int is even num:
'''
for i in range(1,a+1):
    if i%2 == 0:
        b[i]=i**2
print(b)
'''
#sinle line:

'''
d={i:i**2 for i in range(1,a+1) if i%2 == 0  }
print(b)
'''
# 
'''
for i in range(1,a+1):
    if i%2==0:
        b[i]="even"
    else:
        b[i]="odd"
print(b)

e={i:"even" if i%2==0 else "odd" for i in range(1,a+1)}
print(e)
'''

# ____________________________________________________________________________________________________________________________________________________________________________________________
#            Saturday -- mock test for python data structures            Date: 28-02-2026
 
# ____________________________________________________________________________________________________________________________________________________________________________________________
#            Sunday -- holiday                                                            Date: 01-03-2026
 


# ____________________________________________________________________________________________________________________________________________________________________________________________


# Gnerator Comprehension                 Date: 05-03-2026

a=5
'''
d=(i for i in range(a))

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))     # error -- StopIteration

'''
# even numbers:
'''
b=(i for i in range(1,a+1) if i%2 ==0)
print(next(b))
print(next(b))
'''
# if and else odd or even:

'''
c=( f"{i} odd" if i%2==1   else f"{i} even" for i in range(1,a+1) )
for i in range(a):
    print(next(c))
'''


a=[40,20,30,40,50]
lar = a[0]
secl = a[1]

for i in range(len(a)):
    if a[i]>lar:
        secl=lar
        lar=a[i]
    elif secl < a[i] and lar!=a[i]:
        secl=a[i]
print(lar,secl)
        
        


