#Static Method - Inside this method, we don’t use instance or class variable because
# this static method doesn’t take any parameters like self and cls.
class Student:
    college_id=1397
    @staticmethod
    def input_id(a):
        return "Myself Kabir "+ a
kabir=Student()

kabir=Student.input_id("Sidana")
print(Student.input_id("Sidana"))
print(kabir.input_id("Sidana"))