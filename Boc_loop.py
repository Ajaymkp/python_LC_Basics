###__________________________   For Loop     __________________________________________###   Date:11-02-2026

##for i in range(fas):
##    
##    if i in f:
##        f=-i  # not finished
##print(f)



#####   * pattern ########

# 1
'''
for i in range(5):
    print("*")

# 2

for i in range (5):
    print("*",end="")
for i in range(5):    # inside of range (5 == 1,6)    bcz 5=01234, 1,6= 12345  
    print("*",end=" ")
'''
# 3
##n=int(input("Enter a num: "))

'''
for i in range(n):                # based on row to print "*"
    for j in range(n):            # based on column to print "*"
        print("*",end=" ")
    print()
'''

# 4    12345

'''
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
    
# 5

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()  
'''
#6     reverse 54321
'''  
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
    
#7
    
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print() 
'''
  



# 8  op:

##         * * * * *
##         * * * * 
##         * * *  
##         * * 
##         * 
'''  
for i in range(n):
    for j in range(i,n): 
        print("*",end=" ")
    print()
    
# 9   op:
##         *
##         * *
##         * * *
##         * * * *
##         * * * * *                                                                                                                                                                                                             

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''   
   
# 10  op:
##           1 1 1 1 1
##           2 2 2 2
##           3 3 3
##           4 4
##           5
'''
for i in range(1,n+1):
    for j in range(i,n+1): 
        print(i,end=" ")
    print()

# 11    op:
##             1
##             2 2
##             3 3 3
##             4 4 4 4
##             5 5 5 5 5
    
for i in range(1,n+1,):
    for j in range(i):
        print(i,end=" ")
    print()
'''
# 12  op:
#    1
#    2 3
#    4 5 6
#    7 8 9 10

'''

a=1 
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        a+=1
    print()
'''


# 14  Ascii
'''
a=65
for i in range(1,n+1):
    for j in range(1,i+1): 
        print(chr(a),end=" ")
        a+=1
    print()
   
# 15

b=90
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(b),end=" ")
        b-=1
    print()
'''

  ### 16 op:
##                  *
##                * *
##              * * *
##            * * * *
##          * * * * *
'''
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
'''
'''
  ## 17 op:
##             * * * * *
##               * * * *
##                 * * *
##                   * *
##                     *
                      
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    for k in range(n+1 - i):
        print("*",end=" ")
    print()
'''

### triangle      op:  *
##                    * *
##                   * * *
##                  * * * *
##                 * * * * *
'''
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()

##   rev triangle

for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n+2-i):
        print("*",end=" ")
    print()
'''


# 18. diamond [first for triangle AND second for flip triangle]

               # op:
               
##                     * * 
##                   * * * * 
##                 * * * * * * 
##               * * * * * * * * 
##             * * * * * * * * * * 
##             * * * * * * * * * * 
##               * * * * * * * * 
##                 * * * * * * 
##                   * * * * 
##                     * * 

##for i in range(1,n+1):
##    
##    for j in range(1,n+1-i):
##        print(" ",end=" ")
##        
##    for k in range(1,i+1):
##        print("* *",end=" ")
## 
####    for m in range(1,n+1-i):
####        print(" ",end=" ")
##
##    print()
##    
##for o in range(1,n+1):
##    
##    for p in range(1,o):
##        print(" ",end=" ")
##        
##    for q in range(n+1-o):
##        print("* *",end=" ")
##
##    print()


#____________________________________________________________________________________________________________________________________________________________________________________________



####   op:  {usin if}                                           Date: 12-02-2026
##        * 
##      * * 
##    * * * 
##  * * * * 
##* * * * * 

'''
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

###       op:
##            * 
##           * * 
##          * * * 
##         * * * * 
##        * * * * * 

for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ",end="")
        else:
            print("*",end=" ")
    print()
#
print("__________________")


##   op:
##     * * * * * 
##       * * * * 
##         * * * 
##           * * 
##             * 

for i in range(n):
    for j in range(n):
        if j < i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
'''
# reverse
'''
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()


'''
##print("__________________")

s = "python"
##  op:
##      p      
##      p y     
##      p y t    
##      p y t h   
##      p y t h o  
##      p y t h o n 

'''
for i in range(len(s)):
    for j in range(len(s)):
        if j < i+1 :
            print(s[j],end="")
        else:
            print("",end="")

    print()
''' 
#
## #    op:                                home work
##     * 
##     * * * 
##     * * * * * 
##     * * * * * * * 
##     * * * * * * * * *
'''
for i in range(n):
    for k in range(2*n):
        if k < 2*i +1:
            print("*",end=" ")
    print()
'''
##print("__________________")

##n=int()input("Enter a num: ")
## # op;
##             * 
##           * * * 
##         * * * * * 
##       * * * * * * * 
##     * * * * * * * * *
'''
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ",end=" ")
    for k in range(2*n):
        if k < 2*i +1:
            print("*",end=" ")
    print()
'''
#____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                       Date: 13-02-2026

#fascinating number:            (192,219,273,327)

'''
 192
 Step 1: 192 * 2 = 384
 Step 2: 192 * 3 = 576
 Step 3: Concatenate them: 192384576
 Result: This sequence contains 1, 2, 3, 4, 5, 6, 7, 8, and 9 exactly once. Therefore, 192 is a fascinating number.
'''
'''
n=int(input("Enter n: "))
a = n*2
b = n*3
fas=(str(n)+str(a)+str(b))
c=fas.replace("0","")
count=0


for i in range(len(c)):
    for j in range(i+1, len(c)):
        if len(c) != 9 or c[i]==c[j]:
            count+=1
if count == 0:
    print(n ,"is fascinating number")
else:
    print(n ,"is not fascinating number")
'''
### Another method        ## len(c) == 9 is optional
'''
if len(c)==9:
    if ("1" in c) and ("2" in c) and ("3" in c) and ("4" in c) and ("5" in c) and ("6" in c) and ("7" in c) and ("8" in c) and ("9"in c):
        print("Fascinating Number")
else:
    print("Not Fascinating")
'''

# prime number:

'''
num=int(input("Enter a number: "))

for i in range(num+1):

    if i==2 or i==3 or i%2!=0 and i%3!=0:
        print(i,end=" , ")
'''

# Another Method by class reference :
'''
if num < 2:
    print(num ,"is not prime number")
else:
    for i in range(2,num):
        if i%num == 0:
            print(num ,"is not a prime number")
            break
        else:
            print(num ,"is a prime number")
'''      

#____________________________________________________________________________________________________________________________________________________________________________________________

#     saturday did the assesment file                                                                              Date: 14-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#     sundy holiday                                                                                  Date: 15-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#      Monday  (Sir is absent)                                                                Date: 16-02-2026
'''
n=int(input("Enter a number n: "))

if n > 0:
    print(n ,"is a Positive Number")
else:
    print(n ,"is a negative number")
if n%2 == 0:
    print(n ,"is a even number")
else:
    print(n ,"is a odd number")
if n%3 == 0:
    print(n ,"is divisible by 3")
else:
    print(n , "is not divisible by 3")

'''

#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 17-02-2026

# While loop:

'''
while True:
    print("#") ### Infinite printing without break
'''
'''
i=0
while i<5:
    print(i)
    i+=1
'''
# odd numbers print:
'''
i=0
while i<10:
    if i%2==1:
        print(i)
    i+=1
'''
'''
# leap year:
i=0
while i<3000:
    if i%4 == 0 and i%100!=0 or i%400==0:
        print(i)
    i+=1
'''
'''
n=int(input("Enter n: "))
i=0
while i < n:
    i+= n
    if i%4 == 0 and i%100!=0 or i%400==0:
        print(i ,"Leap Year")
    else:
        print(i ,"Not Leap Year")
'''
# Armstrong Number:

'''
n=int(input("Enter a num n: "))
s=str(n)
digit=len(s)
count=0
i=0

while i<len(s):
    count = count + int(s[i])**digit
    i+=1
if n==count:
    print(n ,"is Armstrong number.")
else:
    print(n,"is Not a Armstrong number.")
'''


# perfect:
'''
n=int(input("Enter n: "))
count = 0
i=1

while i<n:
    if n%i == 0:
        count += i
    i+=1
if count == n:
    print("Perfect number")
else:
    print("Not Perfect")
'''       


# *** pattern:

##n=int(input())
i=1
'''
while i<=n:
    j=1
    while j<=n:
        print("*",end=" ")
        j=j+1
    print()    
    i+=1
'''


#

##     * 
##     * * 
##     * * * 
##     * * * * 
##     * * * * * 

'''
    j=1
    while j<i+1:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''

#

##     * * * * *
##     * * * *
##     * * *
##     * *
##     *

'''
while i<=n:
    j=i
    while j<=n:
        print("*",end=" ")
        j+=1
    print()
    i+=1
'''

#      op:
#     n
#     o
#     h
#     t
#     y
#     p
''''
b="python"
i=len(b)-1
while i >= 0:
    print(b[i])
    i-=1
'''

#
##     P 
##     P Y 
##     P Y T 
##     P Y T H 
##     P Y T H O 
##     P Y T H O N
'''
p="PYTHON"
i=0
while i<len(p):
    j=0
    while j<i+1:
        print(p[j],end=" ")
        j+=1
    print()
    i+=1
'''
#
##     P Y T H O N 
##     P Y T H O 
##     P Y T H 
##     P Y T 
##     P Y 
##     P
'''
p="PYTHON"
i=len(p)-1
while i>=0:
    j=0
    while j<i+1:
        print(p[j],end=" ")
        j+=1
    print()
    i-=1
'''

# prime and palindrome:

'''
n=int(input("Enter a num n: "))
count=0
i=2

b=""
k=2
while i < n:
    a=str(i)
    b=a[::-1]
    
    while k < i:

        if i%k==0:
            count+=1
            break
        else:
            count=count
        k+=1

    if b == a and count == 0:
        print(i)
    count, k, b = 0, 2, ""
    i+=1
'''    



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 18-02-2026

 ### Jumping Stetement:

 ### break     ### for loop:
'''   
for i in range(1,10):
    if i==5:
        break           ## stop the loop where condition meets
    print(i)

 ### Continue

for i in range(1,10):
    if i==5:
        continue      ## skip where condition is True 
    print(i)

 ### pass

for i in range(1,6):
    pass             ## for skip the unfinished code

print("Yowaimo")
'''
    ###While loop:

  ### break
'''
i=0
while i < 5:
    if i == 3:
        break
    print(i)
    i+=1

   ### continue

i=0
while i < 5:
    if i==3:
        continue
    print(i)
    i+=1
'''
   ### pass
'''
i=0
while i < 10:
    i+=1
    pass
print("Ace")
'''
'''
password="1234"
i=3
while i > 0:
    n=(input("Enter a password: "))
    if n == password:
        print("Login Successfully")
        break
    else:
        if i == 3:
            print("Incorect Password and you have 2 more attemts")
        elif i == 2:
            print("Incorect Password and you have 1 more attemts")
        elif i == 1:
            print("Incorect Password and you have no more attemts")
    i-=1
'''

 ### List
'''
a=[10,20,30,40,50]

print(a[0])
print(a[4])

# print(a[5])  # error

print(a[2:])   # start
print(a[:3])   # end
print(a[::2])  # step

print(a[::-1])  # reverse or negative step

'''


#____________________________________________________________________________________________________________________________________________________________________________________________
#       List         is mutable means add any data type inside                                                                       Date: 19-02-2026

 ### .append()
'''
a=[10,20,30,40]
b=50

c="ace".upper()

a.append(b)
a.append(60)
print(a)

a.append(c)
print(a)
'''
         ### .index()

##n=[10,20,30]
##m=n.index(20)
##print(m)

'''
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

a.extend("luffy")         ## it will also add but differentiating every sinle letters
a.extend(["sanji"])

print(a)
'''
    ### .insert()
'''
a=[10,20,30]
a.insert(1,15)  # insert in the index what we give
a.insert(3,[40,50,60])

print(a)


 ### replace

b=[10,20,30,40]
b[2] = 50
print(b)


   ### .sort()

s=[10,60,30,70,50,30]

s.sort()
print(s)

  ### .count()

c=s.count(30)       # how many elements in the list
print(c)

  ## .remove()   based on values

s.remove(50)
print(s)

  ### .pop()      # based on index

s.pop()
print(s)
s.pop(1)
print(s)

  ### delete     # del x[:]

d=[1,2,3,4,5]
del d[0:2]
print(d)

'''

  ## .reverse()
'''
r=[10,20,30,40,50]
r.reverse()
print(r)
'''
  ## ..copy()
'''
c=[10,20,30,40]
d=c.copy()
print(d)

c.append([50])
print(c)
print(d)
'''
  ## .clear()

c=[20,40,60]
c.clear()
print(c)

#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 20-02-2026




  ### Tuple

#____________________________________________________________________________________________________________________________________________________________________________________________







#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 21-02-2026





#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 22-02-2026







#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 23-02-2026











#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 24-02-2026

