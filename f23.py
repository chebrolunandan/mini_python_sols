#inheritence

class P:
    def __init__(self,pn):
        self.pname = pn
class C(P):
    def __init__(self,pn,cn):
        self.cname = cn
        P.__init__(self,pn)
    def display(self):
        print("Parent name is ",self.pname)
        print("Child name is",self.cname)
ob = C("john","smith")
ob.display()