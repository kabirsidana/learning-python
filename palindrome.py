# #palindrome number - when we reverse them they remain same
# # num=int(input("Enter Number - "))
# def abc(num):   
#     while(num>1):
#         a=num%10
#         print(int(a),end="")
#         num=num/10

# print("the a is " ,a,"the number is ",num)

# if(num==a):
#     print("yes")
# else:
#     print("no")

num=input("Enter  - ")
a=num[::-1]
print(a)

if(a==num):
    print("yes")
else:
    print("no")