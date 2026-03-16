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
#  op == [24,12,8.6]

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







# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 17-03-2026




# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 18-03-2026










# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 19-03-2026













# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 20-03-2026





# ____________________________________________________________________________________________________________________________________________________________________________________________

#                                                      Date: 21-03-2026
