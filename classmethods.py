#Class Variable - A variable which is declared in the class but 
# not inside a constructor("__init__")
# -> Acessing or Modifying class state without instance variable/method is known as class method
# it takes "cls" as argument and @classmethod decorator or classmethod() function  
class Student:
    college_id=1397
    @classmethod
    def display(cls):
        return  "the clg id is "+ str(cls.college_id)

print(Student.display())
