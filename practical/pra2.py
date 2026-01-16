a=[1,2,3,4,5,6,7,8,9,10]
b=[]
c=[]

odd=list(filter(lambda x:x%2!=0,a))
print("total odd number is",len(odd),"that numbers are",odd)

even=list(filter(lambda x:x%2!=1,a))
print("total even number is",len(even),"that numbers are",even)

for i in a:
    if i%2==1:
        b.append(i)
for i in a:
    if i%2==0:
        c.append(i)

print(b)
print(c)