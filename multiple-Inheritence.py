class Job:
    def __init__(self,name,company):
        print("JOB init")
        self.name=name
        self.company=company
    def method1(self):
        print(" This is method 1 ")
class Sports:
    def __init__(self,game):
        print("Sports init")
        self.game=game
    def method2(self):
        print(" This is method 2 ")
class Student(Job,Sports):
    pass
        # def __init__(self,final):
        #     print("Student init")
        #     self.final=final
        #Super() Function can also be used 
        #job.__init__(self,"kabir","abc")
        #sports.__init__(self, "Cricket")

kabir=Student("kabir", "Apple")

print(kabir.name)
print(kabir.company)
kabir=Sports("cricket")
print(kabir.game2)

