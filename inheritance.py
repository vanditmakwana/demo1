class person:
    def __init__(self,name):
        self.name=name

class emp(person):
    def showrole(self):
        print(self.name,"is employee")

class sal(emp):
    def salary(self,salary1):
        print("that salary is",salary1)

emp1=sal("raj")
emp1.showrole()
emp1.salary(200)