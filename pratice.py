#inheritence
#class P:
 #   def __init__(self,pn):
  #      self.pname = pn
#class c(P):
 #   def __init__(self,pn,cn):
  #      self.cname = cn
   #     P.__init__(self,pn)
    #def display(self):
     #   print("Parent name is ",self.pname)
      #  print("child name is ",self.cname)
#ob = c("nandan","chebrolu")
#ob.display()

#class Student:
 #   def __init__(self):
  #      self.cgpa = 9.0
   # @property
    #def cgpa(self):
     #   print("Getter method invoked")
      #  return self.__cgpa
    #@cgpa.setter
    #def cgpa(self,x):
     #   print("Setter method invoked")
      #  self.__cgpa = x
#ob = Student()
#print(ob.cgpa)
#ob.cgpa = 8.0
#print(ob.cgpa)

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