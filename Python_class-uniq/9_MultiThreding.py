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

# is_alive() method
'''
def func():
    for i in range(5):
        print("shikkai")
def show():
    for i in range(5):
        print("bankai")

t1=Thread(target=func)
t2=Thread(target=show)
print("Before t1",t1.is_alive())  # it will return False because t1 is not started yet
print("Before t2",t2.is_alive())  # it will return False because t2 is not started yet

t1.start()
t2.start()
print("After t1",t1.is_alive())  # it will return True because t1 is started
print("After t2",t2.is_alive())  # it will return True because t2 is started
'''
# active_count() method returns the number of active threads in the current thread's thread group. It includes the main thread and all the threads that are currently running.
#print("Active threads",active_count())  # it will return 3 because main thread, t1 and t2 are active

# active_count() method with time sleep() method 
# main thread will be active until all the threads are completed
'''
def func():
    for i in range(5):
        print("shikkai")
        time.sleep(1)
def show():
    for i in range(5):
        print("bankai")

t1=Thread(target=func)
t2=Thread(target=show)

print("Before t1",t1.is_alive()) 
print("Before t2",t2.is_alive())  

t1.start()
t2.start()

print("Active threads",active_count())
'''

# enumerate() method returns a list of all the active threads in the current thread's thread group. It includes the main thread and all the threads that are currently running.
'''
def func():
    for i in range(5):
        print("shikkai")
        time.sleep(1)
def show():
    for i in range(5):
        print("bankai")
        time.sleep(1)

t1=Thread(target=func)
t2=Thread(target=show)
print("Before t1",t1.is_alive()) 
print("Before t2",t2.is_alive())
t1.start()
t2.start()
print("Active threads",active_count())
print("Enumerate threads",enumerate())  # it will return a list of all the active threads in the current thread's thread group
'''

# process ID -- os.getpid()
'''
import os
from threading import *

def func():
    print("process ID of func",os.getpid())
    print("shikkai")
def display():
    print("process ID of display",os.getpid())
    print("bankai")

t1=Thread(target=func)
t2=Thread(target=display)
t1.start()
t2.start()
print("process ID of main thread",os.getpid())  # it will return the process ID of the main thread
'''


# thread ID -- t1.ident
'''
import os
from threading import *

def func():
    print("thread ID of func",current_thread().ident)
    print("shikkai")
def display():
    print("thread ID of display",current_thread().ident)
    print("bankai")
t1=Thread(target=func)
t2=Thread(target=display)
t1.start()
t2.start()
print("thread ID of main thread",current_thread().ident)  # it will return the thread ID of the main thread
'''

# daemon thread -- a thread that runs in the background and does not block the main thread from exiting. It is used for tasks that are not critical to the main thread and can be safely ignored if the main thread exits.


# Daemon threads are running background
# Daemon threads are used to provide the supports for non daemon thread
# Daemon threads are running continuously in memory
# Garbage collecter is the best example of daemon thread
# Garbage collector is used to delete useless objects from the memory at the time of program execution
# By using daemon property we can set a thread as daemon thread, as well as by using this property we can check s thread is daemon thread or not
# Remember main thread is always non-deamon and we can't change main thread as daemon thread
# Once a thread started then we can't change its nature , so main thread started by pvm , so its not in our hand, that's why we can't change the default nature of main thread.
# Except main thread, remaining all threads nature depends nature depends on its parent, if the parent is daemon, then child also daemon , and vice-versa.
# we can change the nature of other thread except main thread.
# Daemon thread are widely used to maintain log record, grammer checker, scrap data from web in the background.

'''
from threading import *
import time
def func():
    print("func()",current_thread().daemon)
    for i in range(5):
        print("shikkai")
def display():
    print("display()",current_thread().daemon)
    for i in range(5):
        print("bankai")
t1=Thread(target=func)
t2=Thread(target=display)
t1.start()
t2.start()
'''

# daemon thread with time sleep() method -- if the main thread exits then the daemon thread will also exit even if it is not completed
# in real time like bus ticket booking website, we can use daemon thread to maintain log record, if the main thread exits then the daemon thread will also exit even if it is not completed, so it will save the memory and also it will not create any problem because log record is not critical to the main thread.
'''
#
from threading import *
import time
def func():
    print("func()",current_thread().daemon)
    for i in range(5):
        time.sleep(0.5)
        print("shikkai")

t1=Thread(target=func,daemon=True) 
t1.start()
time.sleep(1)
print("main thread is exiting")  # main thread is exiting after 1 second, so the daemon thread will also exit even if it is not completed
'''
#
'''
from threading import *
import time
def func():
    print("func()",current_thread().daemon)
    for i in range(5):
        time.sleep(0.5)
        print("shikkai")
        
def display():
    print("display()",current_thread().daemon)
    for i in range(5):
        time.sleep(1)
        print("bankai")
        
t1=Thread(target=func)
t2=Thread(target=display,daemon=True)
t1.start()
t2.start()
'''



'''
from threading import *
import time
def func():
    print("func()",current_thread().daemon)
    for i in range(5):
        print("shikkai")
def display():
    print("display()",current_thread().daemon)
    for i in range(5):
        print("bankai")
        time.sleep(1)
t1=Thread(target=func)
t2=Thread(target=display)
t2.daemon=True  # it will make t2 a daemon thread
# t2.setDaemon(True)  # it will also make t2 a daemon thread
# t2=Thread(target=diplay,daemon=True) # it will alo make t2 a daemon thread)
t1.start()
t2.start()
'''
# daemon thread inside a normal thread -- it will automatically crete daemon thread because its parent is daemon thread
'''
from threading import *
import time
def func():
    print("func()",current_thread().daemon)
    for i in range(5):
        print("shikkai")
    t2=Thread(target=display)
    t2.start()
    print("t2 is daemon",t2.daemon)  
def display():
    print("display()",current_thread().daemon)
    for i in range(5):
        time.sleep(1)
        print("bankai")
t1=Thread(target=func,daemon=True)
t1.start()
time.sleep(2)
print("main thread is exiting")
'''
# daemon thread inside a non daemon thread -- using daemon=False but its parent is daemon thread
'''
from threading import *
import time

def func():
    print("func()",current_thread().daemon)
    for i in range(5): 
        print("shikkai")
    t2=Thread(target=display,daemon=False)
    t2.start()

def display():
    print("display()",current_thread().daemon)
    for i in range(5):
        print("bankai")
        time.sleep(1)
        
t1=Thread(target=func,daemon=True)
t1.start()
time.sleep(2)
print("main thread is exiting")  
'''

# thread inside a daemon thread -- using daemon=True but its parent is daemon thread
'''
def func():
    print("func()",current_thread().daemon)
    for i in range(5):
        print("shikkai")
    t2=Thread(target=display,daemon=True)  # it will return the current thread object
    t2.start()
def display():
    print("display()",current_thread().daemon)
    for i in range(5):
        time.sleep(1)
        print("bankai")
t1=Thread(target=func)
t1.start()
time.sleep(1)
print("main thread is exiting")
'''







#____________________________________________________________________________________________________________________________________

#                                                                      Date : 11-04-2026
# saturday -- 
#____________________________________________________________________________________________________________________________________

#                                                                      Date : 12-04-2026
# sunday -- holiday
