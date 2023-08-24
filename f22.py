class Student:
    def __init__(self,r,n):
        self.regno = r
        self.name = n
    def display(self):
        print("Register n0 = ",self.regno)
        print("Name = ",self.name)
reg = int(input("enter register no: "))
n = input("enter the name: ")
ob1 = Student(reg,n)
ob1.display()