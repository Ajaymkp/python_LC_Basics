                       ##   variables                               Date: 02-02-2026

## a= 10
##print(a)

## A = 5
##print(A)

#lorem = "adszfxdcbfgfvncvxcdvcbvncxzdsfxfcvgnggfchvjbmnbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                      ## keywords

##if, else, elseif ...

##a= 10
##print(a)
##print(type(a))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                     ##Type cassting

## one type to another type

##a= 10
##b= float(a)
##
##print(b+.4)
##
##print(float(a)+.5)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                  ## input

##b=input("a: ")
##print(b)
##print(float(b)+.5)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                           ##string     
##str="20"
##print(str)
##q= int(str)
##print(q)

##c=int(input("c="))
##print(c)

        ##concat
##a ="Monkey"
##b= "D luffy"
##print(a+b)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                          ## operators
##Arithmatic operator
##Assaignment operator
##comparison operator
##logical operator
##bitwise operator
##identify operator
##membership operator


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                     ##Arithmatic operator

## + - * / %

'''  
a=4
b=6
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a//b)
print(b//a)
print(b%a)
print(a%b)
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                        ##Assaignment operator

## = != += -= *= /= //

##a=6
###a+=5
###a**=2     can only used here not inside print
## a/b
###a//=2     #  // to not  print op in float
##
##print(a)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



            ## comparison operator                                      date:03.02.2026

## return boolean values

## == <=  >= != < > 

##a= 10
##b= 15
##print(10==10)
##print(10==11)
##
##print(a<=b)
##print(50<=10)
##
##print(10>=5)
##print(5>=10)
##
##print(10!=20)
##print(10!=10)
##
##print(4<5)
##print(5)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


          ## logical operator

  ## (Gate)  and or not            (&& || !)
##a=10
##b=20

 #and  (can't put capital)

#3print(a>b & b<a)
##print(a>b and b>a)
##print(a<b and b<a)
##print(a<b and b>a)
## #or 
##print(a>b or b<a)
##print(a>b or b>a)
##print(a<b or b!=a)
##print(a<b or b>a)
##
## #not
##print(a==b)
##print(not(a==b))
##print (a!=b)
##print(not(a!=b))

#s------------------------------------------------------------------------------------------------'
                       #bitwise operator                                        
                 #& and gate

##a=10
##b=12
##print(a&b)
##print(bin(8))
              ## | or gate
##a=3
##b=4
##print(a|b)
##print(7)

             ## ^  xor gate

##a=2
##b=3
##print(a^b)

##p=4
##q=5
##print(a^b)

          ## ~ bitwise not gate ~x = -(x+1)

##f=5
##print(~(f))  #~(-5+1) = -6
##print(bin(~(f)))
##print(bin(-6))
##
##print(bin(~f & 0xff))  # to get cpu's 8-bit values


#-------------------------------------------------------------------------------------------
                      ##membership operator                   Date:04-02-2026

         ## in 
         ## not in
'''
a = "python"
print("o" in a)
print("a" in a)

print("o" not in a)
print("a" not in a)
'''
#--------------------------------------------------------------------------------------
     ## identy operator

           ##is  (check the memory address)    == ()
           ##is not

##z="zoro"
##print(id(z))
'''
a=10
b=11
c=a

print(a is b)
print(a is c)

print(id(a))
print(id(b))
print(id(c))

print(a == b)
print(a == c)

'''

     ## is not
'''
a="luffy"
b="zoro"
c="luffy"

print(a is not b)
print(a is not c)
print(id(a))
print(id(b))
print(id(c))
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


     ## string methods

   #upper
'''
a="abc"
print(a.upper())

a="Abc".upper()
print(a)

print("Zoro".upper())

b=input("Enter your name: ").upper()
print(b)
'''

  # lower
'''
a="Python"
print(a.lower())

a="DEC".lower()
print(a)

c=input("Enter your name: ")
print(c)
'''

 # swap

##a="sanji".swapcase()
##b="SANJI".swapcase()
##print(a,b)


   # capitalize

##a='''i am watching,
##i am eating'''.capitalize()
##print(a)

  #title
##a='''the one piece.
##the one piece is a fiction story'''.title()
##print(a)



   # length()
'''
a="abcd"
print(len(a))

a=input("Enter your name: ")
print(len(a))


   #split()
   
a="Monkey D Luffy"
print(a.split("o"),a.split("f"))

   #replace()
   
a="Black leg Sanji"
print(a.replace("Black leg","Vinsmoke"))
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


  #Ascii values           
'''

A=65
Z=90

a=97
z=122

'''           # max, min, ord, chr

##print(max("Anbu"))   # To find max num values in Ascii
##print(min("Anbu"))   # To find min values in Ascii 
##print(ord('z'))      # To find ascii num value of a variable
##print(chr(97))       # To find variable of a ascii num value
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                # .isalpha(), .isdigit(),  .isupper() & islower()            Date:05-02-2026

a="python"
b="18"
c="SANJI"
'''
print(a.isalpha())
print(b.isalpha())

print(a.isdigit())
print(b.isdigit())

print(c.isupper())
print(a.isupper())

print(a.islower())
print(c.islower())
'''
'''
    # .join()
print("0".join(b))
   # .strip
d= "          leo        "
    
print(d)
print(d.strip())
   # .count()
print(a.count("y"))
'''

  # endwith(), startswith(), sep  
'''
e= "one piece is peak"
print(e.endswith("peak"))  # to check True or Flase end with the word
print(e.endswith("one"))

print(e.startswith("one")) # to check True or Flase start with the word
print(e.startswith("peak"))

print("hi", "hello")
print("hi", "hello",sep="_")

print(c)
print(c, end="!")       #joins in end without space
''' 

#______________________________________________________________________________________________________________________________________________________________________________________________

      #Positive index

f="python"

'''                   # 0  1  2  3  4  5
print(f[0])           # p  y  t  h  o  n
print(f[1])           #-6 -5 -4 -3 -2 -1
print(f[5])
'''

##print(f[6])  # error : out of range

'''
print(f[0:5])  #start &  end

print(f[ :3])  #end  # end value not print in op : pytho
print(f[ :6])

print(f[ : ])  #

print(f[3: ])  #start
print(f[5: ])

'''


 # step
'''
print(f[0:6:1])    #straight   #last ratio is times to read
print(f[6:0:-1])   #reverse
print(f[0:5:2])                 # x-ple
print(f[::2])
'''

#____________________________________________________________________________________________________________________________________________________________________________________________


  #Negative  index                # p  y  t  h  o  n
                                  #-6 -5 -4 -3 -2 -1
'''
print(f[-0])           # 0 or -0 == p
print(f[-1])
print(f[-6])   
'''

#print(f[-7])          # error : out of range
'''
print(f[-6 : -1])   #start and end
print(f[-0 : -1])
print(f[-6 : -3])

print(f[ : -1])    #end  # end value not print in op : pytho
print(f[ : -6])

print(f[ : ])      # 

print(f[-6 : ])    #start
print(f[-1 : ])

'''
'''
       # step

print(f[-6:-1:1])   #straight
print(f[-1:-6:-1])   #revrse
'''
       
#____________________________________________________________________________________________________________________________________________________________________________________________

         ## Conditional statement

   ## if, else, elif

'''
if True:     # True == 1
    print("true")
else:
    print("false")

if False:    # False == 0
    print("true")
else:
    print("false")

'''
'''
if "":           # " " == true  and "" == false without space false
    print("True")
else:
    print("False")
'''




  #pass oor fail
'''
a=int(input("ENTER YOUR MARK: "))

if a>34:
   print("Great you are pass")
else:
    print("Sorry you are fail")
'''    

   # To check odd or even                                          date:06-02-2026
'''
a=int(input("Enter a Number: "))

if a%2 == 1:
    print("odd")
else:
    print("even")
'''

  # to check palindrome:                                       
'''
a=input("enter a word: ")
print(a[ : : -1])

if a == a[ : : -1] :
    print("palindrome")

else:
    print("Is not palindrome")
'''

   # To check Leap year: #######
'''
a=int(input("Enter a year: "))

if a%4 == 0 and a%100 != 0 or a%400 == 0:
    print("Leap year")

else:
    print("It is not Leap year")
'''
    # To check vowels in or not
'''    
a=input("Enter A word: ").lower()
b="aeiou"

if "a" in a or "e"  in a or "i" in a or "o" in a or "u" in a:
    print("vowels")
else:
    print("constants")

'''
#____________________________________________________________________________________________________________________________________________________________________________________________


 # Nested if:
 
'''
m = int(input("Enter a Number: "))

if m > -1 and m < 101:

    if m > 34:
        print("pass")
    else:
        print("fail")

else:
    print("Invali Input")

'''
'''
a=int(input("Enter a year: "))

if a>-1  :
    if a%4 == 0  and a%100 != 0 or a%400 == 0:
        print("Leap year")
    else:
        print("Is not a Leap Year")
else:
    print("invaali input")
'''    
'''
i = int(input("Enter a Number: "))

if i%3 == 0 :
    if i%5 == 0:
        print(i,"is divisible by both 3 and 5")

    else:
        print(i," is divisible by 3 only")
else:
    print(i," is not divisible by 3")
'''

    # graade terms

##    90 - 100    A
##    80 - 89     B
##    70 - 79     C
##    60 - 69     D
##    50 - 59     E
##    0  - 49     RA

  # elif:
'''
j = int(input("Enter your Mark: "))

if 90 <= j <= 100:
    print("GRADE A")
elif 80 <= j <= 89:

    print("GRADE B")
elif 70 <= j <= 79:
    print("GRADE C")
elif 60 <= j <= 69:
    print("GRADE D")
elif 50 <= j <= 59:
    print("GRAADE E")
elif 0 <= j <= 49:
    print("RA")
else:
    print("Invaalid Mark")
'''
#-----------------------------------------------------------------------------------------------

   #  To find max value:                             #   Date:07-02-2026

##a=int(input("Enter a number for a: "))                         
##b=int(input("Enter a number for b: "))
##c=int(input("Enter a number for c: "))
'''
if a<b:
    print("b is greater than a")
elif a>b:
    print("a is greater than b")
else:
    print("a == b")
'''
'''
if a>b and a>c:
    print(a," is the highest value")
elif b>a and b>c:
    print(b, "is the highest value")
elif c>a and c>b:
    print(c, "is the highest value")
else:
    print("a,b and c are same")
'''

##un="sanji"
##pas="abc123"
'''
a=(input("Enter a un for a: "))
b=(input("Enter a pas for b: "))

if a == un and b==pas:
    print(" login successfull")
elif b != pas and un==a:
    print("password is incorrect")
elif un!=a and b==pas:
    print("username unmatched")
else:
    print("Both are wrong")
'''

#Assesment:
   # 1. +,-,*,/,//,**,%
   # 2. leap year
   # 3. palindrome
   # 4. odd or even
   # 5. find the highest value
   # 6. grade

##a=int(input("Enater a num a: "))
##b=int(input("Enter a num b: "))
##c=(input("Enter a operator: "))
   
   ## 1. operator +,-,*,/,//,**,%:
'''  
if c == "+":
    print("sum of a + b =: ",a + b )
elif c == "-":
    print("sutract of a - b: ",a - b)
elif c == "*":
    print("Multple of a*b: ",a*b)
elif c == "**":
    print("Power a**b: ",a**b)
elif c == "/" and b==0:
    print("undifined")
elif c == "/":
    print("Division of a/b: ",a/b)
elif c == "//" and b==0:
s    print("undefined")
elif c == "//":
    print("Division of a//b: ",a//b)
elif c == "%" and b==0:
    print("undefined")
elif c == "%": 
    print("Reminder of a%b: ",a%b)
else:
    print("Invaliid operator")
'''
## 2. leap year
'''
year = int(input("Enter a year: "))
if year%4 == 0 or  year%100 != 0 and year%400 == 0:
    print("Leap year")
else:
    print("Not Leap year")
'''
 ## 3. palindrome
'''
pal = input("Enter a word: ")
rev = pal[::-1]
if pal == rev:
    print("plindrome")
else:
    print("Not Palindrome")
'''
 ## 4. odd or even
'''
oe = int(input("Enter a Num: "))

if  oe%2 == 1:
    print("odd")
else:
    print("even")
'''


 ## 5. find the maximum number
'''
x = int(input("Enter a num x: "))
y = int(input("Enter a num y: "))
z = int(input("Enter a num z: "))

if z<x>y:
    print("x is max")
elif x<y>z:
    print("y is max")
elif x<z>y:
    print("z is max")
else:
    print("all are same")
'''
 ## 6. Grade
"""
Mark = int(input("Enter your Mark: "))

if 89 < Mark <101:   #90-100
    print("Grade A")
elif 79 < Mark < 90: #80-89
    print("Grade B")
elif 69 < Mark < 80: #70-79
    print("Grade C")
elif 59 < Mark < 70: #60-69
    print("Grade D")
elif 49 < Mark < 60: #50-59
    print("Grade E")
elif 34 < Mark < 50: #35-49
    print("pass")
elif -1 < Mark < 35: #0-34
    print("Fail")
else:               
    print("Invalid input")
"""
#____________________________________________________________________________________________________________________________________________________________________________________________



      #                                             Holiday on sunday                                               Date:08-02-2026


#____________________________________________________________________________________________________________________________________________________________________________________________

      #                                                                                            Date:09-02-2026





      
#____________________________________________________________________________________________________________________________________________________________________________________________

      #                                                                                            Date:10-02-2026





      
#____________________________________________________________________________________________________________________________________________________________________________________________

      #                                                                                            Date:11-02-2026


      

















   


