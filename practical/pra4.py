a=[1,1,2,3,3,4,5,5]
b=[]
c=[]
d={1,1,2,3,3,4,5,5}
e={'hello','hii','world'}

for i in a:
    if i in b:
        c.append(i)
    else:
        b.append(i)

print("after remove duplicate",b)
print("duplicate numbers are",c)
print(d)
print(e)