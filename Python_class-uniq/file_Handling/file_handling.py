#                                          Date : 24-03-2026  

# to read by s single line
'''
file=open("aizen.txt", "r")
a=file.readline()
print(a)
file.close()
'''
# to read all the lines in a file we can use readlines() method op in list
'''
file=open("aizen.txt", "r")
a=file.readlines()
print(a)
file.close()
'''
# upto the num lines op in list
'''
file=open("aizen.txt", "r")
a=file.readlines(2)
print(a)
file.close()
'''

#_____________________________________________________________________________________________________________________________________________________________--

#                                          Date : 25-03-2026

#  shpwing us True or False by able to read or not
'''
file=open("aizen.txt","r")
a=file.readable()
print(a)
'''

# here false cuz we denoting to w - writable
'''
file=open("aizen.txt","w")
a=file.readable()
print(a)
'''
# how char's in the file
'''
file=open("aizen.txt","r")
a=file.read()
print(a)
print(file.tell())
file.close()
'''
# 
'''
file=open("aizen.txt","r")
a=file.read()
a=file.read()  # no work for this here
file.close()
'''
#
'''
file=open("aizen.txt","r")
a=file.read(10)
a=file.read() # here works after 2nd line
file.close()
'''
#
'''
file=open("aizen.txt","r")
a=file.readline()
a=file.readline()
file.close()
'''
#
'''
file=open("aizen.txt","r")
a=file.readlines(2)
a=file.readlines()
file.close()
'''
# seek -- op in showing where the needle 
'''
file=open("aizen.txt","r")
print(file.read())
print(file.tell())
file.seek(10)
print(file.tell())
print(file.read)
file.close()
'''
# Alternate for fil=open(0 and file.close)
'''
with open("aizen.txt","r") as f:
    print(f.read())
'''

# to write new line and it will delete all text in the file
'''
file=open("aizen.txt","w")
file.write("yowaimo")
file.close()
'''
# to write multiple lines

'''
file=open("aizen.txt","w")
file.write("yo zoro\n")
file.write("see you luffy\n")
file.close
'''
# To write list by writelines
'''
i=["yokoso\n","watashimo soul society\n","yare yare kokedhana\n"]
file=open("aizen.txt","w")
file.writelines(i)
file.close
'''  

# print of write means how many char's in the write ""
'''
file=open("aizen.txt","w")
print(file.tell())
file.write("yo des")
print(file.tell())
file.seek(3)
print(file.write("kombawa tamaya san"))
file.close()
'''
#
'''
file=open("aizen.txt", "w")
file.seek(5)
file.write("try new")
file.close()
'''
#
'''
file=open("aizen.txt", "w")
file.write("espada ")
file.seek(7)
file.write("grimjow")
file.close()
'''
# to create new file
'''
file=open("bleach.txt","x")
file.close()
'''
# to write in new file
'''
with open("bleach.txt","w") as f:
    f.write("bleach is a good anime")
'''
# to append in the file
'''
with open("bleach.txt","a") as f:
    f.write("\n Bankai is the best")
'''
#to seek 
'''
with open("bleach.txt","a") as f:
    f.seek(40)
    f.write("Shikkai")
'''
# append multiple lines
'''
with open("bleach.txt","a") as f:

    f.write("\nnel")
    f.write("\ngrimjow")
    f.write("\nyachiru")
'''
# append list by writelines
'''
a=["\nchad","\nishida","\nichigo"]
with open("bleach.txt","a") as f:
    f.writelines(a)
'''
# rewrite the file 
# It can read and write but it will not clear the content in the file and it can not create new file
'''
with open("aizen.txt", "r+") as f:
    print(f.read())
'''
#

'''
with open("aizen.txt", "r+") as f:
    f.write("new content")
'''

# 
'''
with open("aizen.txt", "r+") as f:
    print(f.read())
    f.seek(7)
    f.write("yokoso")
'''

# 
'''
with open("aizen.txt", "r+") as f:
    print(f.read())
    f.write(" matha na")
'''

# clear all content in w+
# And w+ is for read and write but it will clear all content in the file
# It can create new file
'''
with open("aizen.txt", "w+") as f:
    f.write("yo zoro")
    f.seek(0)          # if it is not there then it will print nothing
    print(f.read())
'''
# a+ is for read and write but it will not clear the content in the file
# It can create new file
'''
with open("aizen.txt", "a+") as f:
    f.write("\nwhite")
    f.seek(0)
    print(f.read())
'''

# to append and read
# here seek is important to read the content in the file because if we not use seek then it will print nothing because the pointer is at the end of the file
'''
with open("aizen.txt", "a+") as f:
    print(f.tell())
    f.seek(0)
    print(f.read())
    f.write("\nzangetsu")
'''

#_____________________________________________________________________________________________________________________________________________________________--

#                                          Date : 26-03-2026

# img -- rb
'''
file=open("luf.jpg","rb")
a=file.read()
print(a)
file.close()
'''
# img copy
'''
f1=open("luf.jpg","rb")
f2=open("luf_copy.jpg","wb")
for i in f1:
    f2.write(i) 
f1.close()
f2.close()
'''
# pickle dump -- to write in file by pickle
'''
import pickle
file=open("aizen.txt","wb") 
a={"name":"ichigo","age":15,"hobby":"fighting"}
x=pickle.dump(a,file)
file.close()
'''

# to write in file by pickle
'''
import pickle
file=open("aizen.txt","wb")
a="name"
print(a)
file.close()
'''

# pickle.load -- to read the file by pickle
'''
import pickle
file=open("aizen.txt","rb")
x=pickle.load(file)
print(x)
file.close()    
'''

#________________________________________________________________________________________________________________-


#  file handling                               Date:27-03-2026


# remove file
'''
import os
os.remove("text.txt")
'''

# checking file is exist or not
'''
import os
if os.path.exists("bleach.txt"):
    print("yes")
else:
    print("No")
'''
#