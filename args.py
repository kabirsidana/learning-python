# *args is used to pass number of variable in a function
"""
subjects={"english":"mam1","hindi":"sir2"}
def func1(*args):
    for key, value in subjects:
        print(key,value)
func1(*subjects)
"""
# similarly we use **kwargs for dictionarys
dict1={"foe":"enemy","bro":"brother","loomy":"sad","binary":"two"}
def kwargss(**a):
    for key, value in dict1.items():
        print(key, value)
kwargss(**dict1)
