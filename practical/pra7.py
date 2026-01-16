a={1,2,3,4,5}
b={4,5,6,7,8}
c=[1,2,3,4,5]
d=[4,5,6,7,8]
e=[]

print("first set is",a)
print("first set is",b)

for i in c:
    if i in d:
        if i not in e:
            e.append(i)
print("common element in both is(using list)",e)

f=a.intersection(b)
print("common element in both is(using set)",f)