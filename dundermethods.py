class Employee:
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
    def __add__(self,other):
        return self.salary+other.salary
    def __truediv__(self,other):
        return self.salary//other.salary
    def __mul__(self,other):
        return self.salary*other.salary    
kabir=Employee(1234,19)
rahul=Employee(88,21)
print(kabir+rahul)
print(kabir/rahul)
print(kabir*rahul)