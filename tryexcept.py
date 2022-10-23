#If we have any doubt regarding any statement or function
# we can use try except and it will try and print the error as a string if it not well
# it will run the remaining concept properly without any problem
# without it the final Statement will not be executed 
num1=int(input("Enter Number 1  ->   "))
num2=int(input("Enter Number 2  ->   "))
#normally showing the error or wrong input
"""try:
    print(a/b)
except:
    print("Sorry Wrong input")
finally:
    print("this statement is used after try except and this will always be exceuted")
    """
#catching the error and printing as a string
try:
    print("the sum of both values is    ", a+b) #wrong statement
except Exception as c: #we catch the error and stored in c and it will print like a string
    print(c)


print("---Final Statement ---")