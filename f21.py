class Student:
    def __init__(self,r,n):
        self.regno = r
        self.name = n
    def display(self):
        print("Register no = ",self.regno)
        print("Name = ",self.name)
ob1 = Student(2100090004,"Nandan")
ob2 = Student(2100090000,"Sid")
ob1.display()
ob2.display()