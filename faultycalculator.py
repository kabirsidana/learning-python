    # We have to make a normal calcultor but it should wrong answer for these equations
    # 45*3=555
    # 56+9=77
    # 56/6=4
def repeat():
    print("THIS CALCULATOR IS MADE BY KABIR ")
    print("Choose and Operator "); print("Addition -> + ");print("Subtraction -> - ");print("Multiplication -> *");print("Division -> / ")
    print("Modulas -> %");
    print("Square -> ** ")

    c = input("Enter the Operator +,-,/,*  ")
    a = int(input("Enter the First Number  "))
    b = int(input("Enter the Second Number  "))
    if c == "*":
        if a == 45 and b == 3:
            print(555)
        else:
            print(a*b)

    if c == "+":
        if a == 56 and b == 9:
            print(77)
        else:
            print(a+b)


    if c == "/":
        if a == 56 and b == 6:
            print(4)
        else:
            print(a/b)

    if c == "-":
        print(a-b)

    if c == "**":
        print(a**b)
repeat()
a=input("Do you run the calculator again y for yes ,n for   ")
if(a=="y"):
    repeat()
else:
    print("OK GOOD BYE")
