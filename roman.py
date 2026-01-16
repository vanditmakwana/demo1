def isEven(n):
    a=n%2
    if a ==0:
        return True 
    else:
        return False
    
if __name__=="__main__":
    n=int(input("enter number "))
    if isEven(n):
        print("true")
    else:
        print("false")
