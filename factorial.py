#Factorial is n* n-1 , 5!=120, 5*4*3*2*1
#In Maths factorial of zero is always one , 0!=1
print("---This Program Will Find Factorial ---")
num=int(input("Enter the Number Here"))
f=1
for i in range(1,num+1):
    f=f*i
print(f)

#anoter way
"""
a=int(input("enter a number here"))
# for i in range(1,a):
b=1
while(a>0):
    b=b*a
    a-=1
print(b)

"""


