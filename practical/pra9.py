dict1={
    "raj":10,
    "sid":20,
    "rohan":30
}

a=input("enter a student ")

if a in dict1:
    print("mark of",a,"=",dict1[a])
else:
    print("student not found")