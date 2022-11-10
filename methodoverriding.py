''' When a child class method overrides the parent class method of 
 same name, parameters and return type, it is known as method overriding.'''

 
class A:
    instance_var=" This is a Normal Variable "
    def __init__(self):
        self.instance_var=" This is Instance Variable "
        self.special="This is a Special Function"
class B(A):
    def __init__(self):
        
        self.instance_var="This is a Instance Variable of Class B"
        pass

ob=B()
print(ob.instance_var)
'''Unable to run this method because the constructor is overridden'''
#print(ob.special)


