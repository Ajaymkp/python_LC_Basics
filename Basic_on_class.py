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
'''

  #split()
a="Monkey D Luffy"
print(a.split("o"),a.split("f"))

   #replace()
a="Black leg Sanji"
print(a.replace("Black leg","Vinsmoke"))

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


  #Ascii values
'''

A=65
Z=90

a=97
z=122

'''








   


