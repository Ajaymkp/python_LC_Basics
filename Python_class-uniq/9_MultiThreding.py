#____________________________________________________________________________________________________________________________________

#                                                                      Date : 08-04-2026
from threading import *
import time

# currentthread() -- single thread

'''
def func():
    print("func()", current_thread().name)
    for i in range(5):
        print("Yo")
def display():
    print("display", current_thread())
    for i in range(5):
        print("see you")
func()
display()
'''

# multithread
'''
def func():
    print("func()",current_thread().name)
    for i in range(5):
        print("Yo")
def display():
    print("display()",current_thread().name)
    for i in range(5):
        print("see you")

t1=Thread(target=func,name="aizen")
t2=Thread(target=display,name="urahara")        
t1.start()
t2.start()
'''

# possible to pass arguments to the thread
'''
def func(n):
    print("func()",current_thread().name)
    for i in range(5):
        print(n)
def display(m):
    print("display()",current_thread().name)
    for i in range(5):
        print(m)
t1=Thread(target=func,args=("Yo",))
t2=Thread(target=display,args=("see you",))
t1.start()
t2.start()
'''

#keword arguments
'''
def func(m,n):
    print("func()",current_thread().name)
    for i in range(5):
        print(m+n)
def display(x,y):
    print("display()",current_thread().name)
    for i in range(5):
        print(x+y)
t1=Thread(target=func,kwargs={"m": "Yo","n": "koso"})
t2=Thread(target=display,kwargs={"x": "see ","y": "you"})
t1.start()
t2.start()
'''
# 
'''
def func():
    for i in range(5):
        print("Yo")
def display():
    for i in range(5):
        print("see you")
s=time.time()
func()
display()
e=time.time()
print("Time taken",e-s)
'''

#
'''
def func():
    for i in range(5):
        print("Yo")
def display():
    for i in range(5):
        print("see you")

t1=Thread(target=func)
t2=Thread(target=display)

s=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
e=time.time()
print("Time taken",e-s)
'''

# class threading
'''
class A:
    def func(self):
        for i in range (5):
            print("Yo")
    def display(self):
        for i in range(5):
            print("see you")
a=A()
t1=Thread(target=a.func)
t2=Thread(target=a.display)
t1.start()  
t2.start()
'''
# arbitrary positional arguments in class threading

'''
class A:
    def func(self,a):
        for i in range (5):
            print(a)
    def display(self,m):
        for i in range(5):
            print(m)
a=A()
t1=Thread(target=a.func,args=("Yo",))
t2=Thread(target=a.display,args=("see you",))
t1.start()
t2.start()
'''

# Arbitary keyword arguments
'''
class A:
    def func(self,a,b):
        for i in range (5):
            print(a+b)
    def display(self,m,n):
        for i in range(5):
            print(m+n)
a=A()
t1=Thread(target=a.func,kwargs={"a": "Yo","b": "koso"})
t2=Thread(target=a.display,kwargs={"m": "see ","n": "you"})
t1.start()
t2.start()
'''
#____________________________________________________________________________________________________________________________________

#                                                                      Date : 09-04-2026
# inheriting Thread class so no need for target and args
'''
class A(Thread):
    print("A class",current_thread().name)
    def run(self):
        for i in range (5):
            print("Bankai")
class B(Thread):
    print("B class",current_thread().name)
    def run(self):
        for i in range(5):
            print("Shikai")
a=A()
b=B()
a.run()  # normal function call so it will run in main thread
b.run()
'''
# to run in separate thread we need to call start() method
'''
class A(Thread):
    
    def run(self):
        print("A class",current_thread().name)
        for i in range(5):
            print("Bankai")
class B(Thread):
    def run(self):
        print("B class",current_thread().name)
        for i in range(5):
            print("Shikai")
a=A()
a.start() 
b=B()
b.start()
'''

# time sleep() method
'''
def func():
    for i in range (5):
        print("Bankai")
        time.sleep(1)
def display():
    for i in range(5):
        print("Shikai")
func()
display()
'''
# time sleep() method in multithreading
'''
def func():
    for i in range (5):
        print("Bankai")
        time.sleep(1)
def display():
    for i in range(5):
        print("Shikai")
        time.sleep(1)
t1=Thread(target=func)
t2=Thread(target=display)
t1.start()
t2.start()
'''

# init thread
'''
class A(Thread):
    def __init__(self,m):
        Thread.__init__(self)
        self.m=m
    def run(self):
        for i in range(5):
            print(self.m)

class B(Thread):
    def __init__(self,n):
        Thread.__init__(self)
        self.n=n
    def run(self):
        for i in range(5):
            print(self.n)
a=A("Bankai")     # here order is important because we are passing argument to the constructor and it will be used in run method
a.start()
b=B("Shikai")
b.start()
'''
    
# join() method
'''
def func():
    for i in range(5):
        print("shikkai")
def show():
    for i in range(5):
        print("bankai")
def display():
    for i in range(5):
        print("kyoka suigetsu")
t1=Thread(target=func)
t2=Thread(target=show)
t3=Thread(target=display)
t1.start()
t2.start()
t1.join()  # it will wait for t1 to complete and then it will start t3
t3.start()

'''

# join() method with timeout
'''
def func():
    for i in range(5):
        print("shikkai")
def show():
    for i in range(5):
        print("bankai")
def display():
    for i in range(5):
        print("kyoka suigetsu")
t1=Thread(target=func)
t2=Thread(target=show)
t3=Thread(target=display)
t1.start()
t2.start()
t2.join(1)  # it will wait for t2 to complete for 1 second and then it will start t3
t3.start()

'''

# time taken by join() method with timeout
'''
def func():
    for i in range(5):
        print("shikkai")
        time.sleep(1)
def show():
    for i in range(5):
        print("bankai")
def display():
    for i in range(5):
        print("kyoka suigetsu")
t1=Thread(target=func)
t2=Thread(target=show)
t3=Thread(target=display)
t1.start()
t2.start()
t2.join(3)  # it will wait for t2 to complete for 3 seconds and then it will start t3
t3.start()
'''
#
'''
def func():
    time.sleep(1)
    t3.join()  # it will wait for t3 to complete and then it will start t1
    for i in range(5):
        print("shikkai")
        
def show():
    for i in range(5):
        print("bankai")
def display():
    for i in range(5):
        print("kyoka suigetsu")
t1=Thread(target=func)
t2=Thread(target=show)
t3=Thread(target=display)
t1.start()
t2.start()
t3.start()
'''

# 
'''
def func():
    for i in range(5):
        print("shikkai")
def show():
    for i in range(5):
        print("bankai")
def display():
    for i in range(5):
        print("kyoka suigetsu")
t1=Thread(target=func)
t2=Thread(target=show)
t3=Thread(target=display)
t1.start()
t1.join()  # it will wait for t1 to complete and then it will start t2
t2.start()
t2.join()  # it will wait for t2 to complete and then it will start t3
t3.start()
'''

# Thread name we can set thread name by using name parameter in Thread() constructor or by using setName() method

'''
def func():
    print("func()",current_thread().name)
    for i in range(5):
        print("shikkai")
def display():
    print("display()",current_thread().name)
    for i in range(5):
        print("bankai")
t1=Thread(target=func)
t1.name="aizen"
t2=Thread(target=display)
t2.name="urahara"

t1.start()
t2.start()
'''

#____________________________________________________________________________________________________________________________________

#                                                                      Date : 10-04-2026


#____________________________________________________________________________________________________________________________________

#                                                                      Date : 11-04-2026
# saturday -- 
#____________________________________________________________________________________________________________________________________

#                                                                      Date : 12-04-2026
# sunday -- holiday
