
## Assesment_sat_28-03-2026

# python

# 1. Longest common prefix:

'''
a=["flower","flow","flight"]
b=a[0]
for i in range(1, len(a)):
    while not a[i].startswith(b):
        b=b[0:len(b)-1]
print(b)
'''
# 2. op : [[1,1,1],[2,2,2],[3,3],[4]]
'''
a=[1,2,3,1,2,3,4,1,1,2]
a.sort()
b=[]
c=[a[0]]
for i in range(1,len(a)):
    if a[i] == c[0]:
        c.append(a[i])
    else:
        b.append(c)
        c=[a[i]]
b.append(c)
print(b)
'''
# 3. Longest substring:
'''
a="abaacbd"
b=set()
l=0
length=0

for i in range(len(a)):
    while a[i] in b:
        b.remove(a[l])
        l+=1
    b.add(a[i])
    length = max(length,i-l+1)   
print(length)
'''
# 4. second most frequent number:
'''
a=[2,3,1,3,2,4,2]
b={}

for i in a:
    b [i] =a.count(i)
print(b)
c=[]
for i,j in b.items():
    c.append((i,j))
print(c)
d=sorted(c,key=lambda x:x[1],reverse=True)
print(d)
print(d[1][0])
'''
# 5. op -- a1b2c3d4e5
'''
a="abbcccddddeeeee"
b=list(a)
c={}
d=""
for i in b:
    c [i] = b.count(i)
print(c)

for i,j in c.items():
    d+=i
    d+=str(j)
print(d)
##e=sorted(list(c.items()),key=lambda x:x,reverse=True)
##print(e)
'''
