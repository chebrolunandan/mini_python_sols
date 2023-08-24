class Student:
    def __init__(self):
        self.cgpa = 9.0
    @property
    def cgpa(self):
        print("Getter method invoked")
        return self.__cgpa
    @cgpa.setter
    def cgpa(self,x):
        print("Setter method invoked")
        self.__cgpa = x
ob=Student()
print(ob.cgpa)
ob.cgpa = 8.0
print(ob.cgpa)

