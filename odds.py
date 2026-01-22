x=[1,2,3,4]
y=10
names = ["A", "B"]
marks = [90, 80]
print(id(y))
print(type(y))

for n, m in zip(names, marks):
    print(n, m)

del x[0]
print(x)