#Public Access Specifier(Default) -> easily accessible from any part of the program
class Student:
    def __init__(self,name,age):
        #public data members
        self.Sname=name
        self.Sage=age

        #public member function
    def display(self):
        #accessible to functions
        print(self.Sname)
        print(self.Sage)

kabir=Student("Kabir", 19)
#accessing with method
kabir.display()
#accessible directly
print(kabir.Sname)