#fstring helps us to call variables as well as we can call functions or do sums in ""
#Method 1
name="kabir"
age=19
#writing f is important before ""
a=f"My Name is {name} AND My Age is {age}"
print(a)
#Method 2
subject="BCA"
state= "Rajasthan"
b="My subject is {} And I Live in {}"
c=b.format(subject,state)
print(c)