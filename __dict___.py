#The __dict__ in Python represents a dictionary or any mapping object 
# that is used to store the attributes of the object

class school:
    dresscode=1212

kabir=school()
rahul=school()

kabir.name="Myself Kabir"
kabir.id="1"
rahul.name="Myself Rahul"
rahul.id="2"
'''
print(kabir.dresscode)
print(kabir.dresscode)
'''
print(kabir.__dict__)
kabir.dresscode=999
print(kabir.__dict__)