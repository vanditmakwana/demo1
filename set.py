a={"krish","jay"}
b={"ram","shyam"}
c={1,2,3,4,5}
d={3,4,6,7,8}
set1=set()
for i in range(5):
    set1.add(i)
print(a)
print(b)
print(c)
print(d)
print(set1)

# for i in range(1,6):
#     a.add(i)
# print(a)

pop=a.union(b)
print(pop)

pop=a|b
print(pop)

e=c.intersection(d)
print(e)

f=c.difference(d)
print(f)

g=c.symmetric_difference(d)
print(g)

print(c.__sizeof__())
for i in a.__iter__():
    print(i)