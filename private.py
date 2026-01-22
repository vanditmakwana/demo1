class person:
    def __init__(self,age):
        self.__age=age
        # self.name=name
    def get_age(self):
        return self.__age

p=person(80)
print(p.get_age())
# p=person("raj",43)
# print(p.__age)