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
n=int(input("Enter a num: "))

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
    ### reverse

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
##       * * * * * 
##       * * * *  
##       * * *   
##       * *    
##       *

for i in range(n):
    for j in range(n):
        if j < n-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("__________________")
##   op:
##       * * * * * 
##       * * * *  
##       * * *   
##       * *    
##       *   
for i in range(n):
    for j in range(n):
        if j > n-i-1:
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
#
'''
print("__________________")

s = "python"
##  op:
##      p      
##      p y     
##      p y t    
##      p y t h   
##      p y t h o  
##      p y t h o n 


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

for i in range(n):
    for k in range(2*n):
        if k < 2*i +1:
            print("*",end=" ")
    print()

print("__________________")

##n=int()input("Enter a num: ")
## # op;
##             * 
##           * * * 
##         * * * * * 
##       * * * * * * * 
##     * * * * * * * * *
for i in range(n):
    for j in range(n):
        if j < n-i-1:
            print(" ",end=" ")
    for k in range(2*n):
        if k < 2*i +1:
            print("*",end=" ")
    print()

#____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                       Date: 13-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________

#                                                                                       Date: 14-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 15-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 16-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 17-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 18-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 19-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                       Date: 20-02-2026



#____________________________________________________________________________________________________________________________________________________________________________________________
