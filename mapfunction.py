#MAP FUNCTION - it apply function to whole iterable
#This is the way to convert every element in int with for loop
"""
a=["12","13","99"]
for i in range(len(a)):
    a[i]=int(a[i])
print(a[1]+17)
"""
#we can also do it with map() function
"""
lst=["12","13","65","2322"]
lst=list(map(int, lst))
print(lst[2]+4)
"""
#Another example of map()
"""
lst=[12,34,23,22,15,4,3,6]
def sq(a):
    return a*a
lst=list(map(sq,lst))
print(lst)    
"""
#map() with Lambda 
"""
lst=[12,34,23,22,15,4,3,6]     
lst=list(map(lambda x:x*x, lst))
print(lst)
"""
