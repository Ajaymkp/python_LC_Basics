  ###      Assesment  10 problems    Date:14-02-2026

#1 factorial:
'''
f=int(input("Enter a num f: "))
fac=1
for i in range(1,f+1):
    fac=i*fac
print(fac)
'''
#___________________________________________________________________

#2 perfect number:
'''
p=int(input("Enter a num p: "))
count=0
for i in range(1,p):
    if p%i == 0:
        count+=i
if count == p:
    print(p, "is a perfect number")
else:
    print(p, "is not a perfect number")    
'''

#3 Armstrong Number:
'''
a=int(input("Enter a num a: "))
b=str(a)
digit=len(b)
arm=0

for i in (b):
    arm= arm + (int(i)**len(b))
    
if arm == a:
    print(a, "is a Armstrong number")
else:
    print(a, "is not Armstrong number")    
'''
#4 Fibonacci series:
'''
fi=int(input("Enter a num fi: "))
a=0
b=1
for i in range(fi+1):
    print(a)
    a,b=b,a+b
'''
#5 fascinating:
'''
f=int(input("Enter a num f: "))
g= str(f) + str(f*2) + str(f*3)
h=g.replace("0", "")
count=0
for i in range(len(h)):
    for j in range(i+1,len(h)):
        if len(h)!=9 or h[i]==h[j]:
            count+=1
if count == 0:
    print(f, "is a Facsinating number")
else:
    print(f, "is not Fscinaating number")    
'''
#6 Leap year:

'''
l=int(input("Enter a Year: "))

if l%4==0 and l%100!=0 or l%400==0:
    print(l ,"is a Leap Year")
else:
    print(l ,"is not a Leap Year")
'''
   

##7      *
##     * * *
##   * * * * *
'''
n=int(input("Enter a number n: "))

for i in range(n):
    for j in range(2*n):
        
        if j < n-i-1:
            print(" ",end=" ")
            
    for k in range(2*n):
        
        if k < 2*i+1:
            print("*",end=" ")
    print()  
'''        
#8 prime number:


num=int(input("Enter a number: "))
'''
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
            break
'''        
#9 reverse string:
'''
r=input("Enter a string: ") 
a=""
for i in (r):
    a=i+a
print(a)
'''
#10 vowels count
'''
v=input("Enter a string: ").lower()
count=0
for i in (v):
    if i in "aeiou":
        count+=1
print(count)
'''




























    
