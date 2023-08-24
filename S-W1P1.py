class Employee:
    __id=0
    __firstname=""
    __lastname=""
    __department=""
    __designation=""
    __doj=0
    __email=""
    __mobile=""
    def setData(self):
        self.__id=int(input("Enter Id\t:"))
        self.__firstname = input("Enter firstname\t:")
        self.__lastname = input("Enter lastname\t:")
        self.__department = input("Enter department:")
        self.__designation = input("Enter designation\t:")
        self.__doj = int(input("Enter doj:"))
        self.__email=input("Enter email:")
        self.__mobile=int(input("Enter mobile number:"))
    def showData(self):
        print("Id\t\t:",self.__id)
        print("FirstName\t:", self.__firstname)
        print("LastName\t:", self.__lastname)
        print("Department\t:", self.__department)
        print("Designation\t:", self.__designation)
        print("DOJ\t:", self.__doj)
        print("Email\t:", self.__email)
        print("Mobile\t:", self.__mobile)

def main():
    #Employee Object
    emp=Employee()
    emp.setData()
    emp.showData()

if __name__=="__main__":
    main()
