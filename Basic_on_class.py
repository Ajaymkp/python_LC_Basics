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
if True:
    print("true")
else:
    print("false")

if False:
    print("true")
else:
    print("false")
'''
  #pass oor fail
'''
a=int(input("ENTER YOUR MARK: "))

if a>34:
   print("Great you are pass")
else:
    print("Sorry you are fail")
'''    

   # To check odd or even
'''
a=int(input("Enter a Number: "))

if a%2 == 1:
    print("odd")
else:
    print("even")
'''

#____________________________________________________________________________________________________________________________________________________________________________________________


 #                                                                           date:06-02-2026




























   


