a=list(map(int,input("enter numbers ").split()))
min1=a[0]
max1=a[0]

for num in a:
    if num < min1:
        min1=num
    if num > max1:
        max1=num
print("minimum number(using loop)",min1)
print("maximum number(using loop)",max1)

b=min(a)
print("minimum number is ",b)

c=max(a)
print("maximum number is ",c)   