#It is very similar to Constructor  and  The __init__  function is called every time an object is created from a class
#  The __init__ method lets the class initialize the object’s attributes
class school:
    def __init__(self,maths,science,computer):
        self.maths=maths
        self.science=science
        self.computer=computer

harry=school("pass","fail", "grace")
print(harry.maths)
print(harry.computer)
print(harry.science)