test="hello world"
a={}
words=test.split()
   
for i in words:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
print(a)