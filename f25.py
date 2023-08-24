class Student:
    def __init__(self,x):
        self.name = x
    @property
    def name(self):
        print("Getter method invoked")
        return self.__name
    @name.setter
    def name(self,y):
        print("Setter method invoked")
        self.__name = y
x = input("Enter name ")
ob=Student(x)
print(ob.name)
ob.name = "Nandu"
print(ob.name)
