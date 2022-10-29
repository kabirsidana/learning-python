#Self 
# It is the instance of the class , it changes value according to the need

class get_info():
    def printmarks(self):
        return f"{self.name} is {self.maths} in maths and {self.english} in english"
rahul=get_info()
rahul.name="rahul singh"
rahul.maths="pass"
rahul.english="fail"

kabir=get_info()
kabir.name="kabir singh"
kabir.maths="pass"
kabir.english="pass"

print(rahul.printmarks())
print(kabir.printmarks())
