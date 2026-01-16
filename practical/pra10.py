s=input("Enter the string ")
a={}

for i in s:
        if i in a:
            a[i]=a[i]+1
        else:
            a[i]=1
print(a)