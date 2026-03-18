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

z=sorted (y, key=lambda x:x[1], reverse=True)
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
# and divide by input by increacing 1
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

# op -- [3,4,5,1,2]  -- change upto input  index 
'''
x=[1,2,3,4,5]
y=2
z=x[y:]+x[:y]
print(z)
'''
# change upto iput index to last
'''
a=[1,2,3,4,5]
b=int(input())

for i in range(k):
    x=a.pop(0)
    a.append(x)
print(a)
'''
# change input only to last 

'''
a=[1,2,3,4,5]
b=int(input())
j=a[0]
for i in range(len(a)):
    if a[i] == b:
        a.remove(b)
        a.append(b)
        break
print(a)
'''

##      non repeating string 
        

'''
x="aabccc"
y=list(x)
for i in y:
    z=y[len(y):i:-1]
    if  i in z:
        y=pop(i)
print(y)
'''
# Another Method
'''
x="aabccc"
def func(a):
    for i in a:
        if a.count(i)==1:
            return i
print(func(x))
'''
# Another Method

'''
a="aabbccc"
for i in a:
    if a.count(i)!=1:
         print(None)
         break
    else:
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
# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 17-03-2026

#longest substring without duplicate values
'''
x="bankaitensazangatsu"
##x="abadbc"
s=set()
l=0
length=0

for r in range(len(x)):
    while x[r] in s:
        s.remove(x[l])
        l+=1
    s.add(x[r])
##    if length>r-l+1:
##        length = length
##    else:
##        length = r-l+1
    length=max(length,r-l+1)
print(length)
'''            
    
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
x=[1,1,1,2,2,3,3,3,4,4]
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

    
##a=x[0]
a=sorted(y,key=lambda b:(len(b),b[0]) ,reverse=True)
print(a)

##b=[y[0]]
####b.insert(0,y[2])
##
##for i in range(1,len(y)):
##    
##    if len(y[i]) > len(b[i-1]):
##        b.insert(i,y[i])
##    elif len(y[i])==len(b[i-1]):
##        b.insert(i-1,y[i])
##    else:
##        b.append(y[i])
##print(b)


### ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 18-03-2026










# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 19-03-2026













# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 20-03-2026





# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 21-03-2026
