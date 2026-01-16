a=[1,2,3,4,5,6]
total=0
avg=0
print("original list",a)

b=sum(a)
print("sum using sum function",b)

for i in a:
    total=total+i
print("sum using loop",total)

avg=total/len(a)
print("average is",avg)