a=[1,2,3,4,5]
print("original list is ",a)

b=a[::-1]
print("reversed list (using slicing) is ",b)

a.reverse()
print("reversed list (using reverse function)",a)