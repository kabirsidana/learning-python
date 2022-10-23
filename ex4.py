#Exercise of printing pattens and taking input as number of rows and a boolean variable(0 or 1)
#if the value is 1 then print in ascending order 
#if the value is 0 then print in descending order
 
user_input=bool(input("Enter 1 or 0 ->   ")) #boolean variable
rows=int(input("Enter Number of Rows ->   "))
if user_input==1:
    for i in range(0,rows):    # we will take range from 1 to number of rows +1
        print("*"*i,"\n")      #the value of i will change according to loop and we will multiple it
if user_input==0:
    for j in range(rows,0,-1): # here we will slice the string -1 at end will reverse the string
        print("*"*j,"\n")



    #another way

    """ 
     
user_input=int((input("Enter 1 or 0 ->   "))) #boolean variable
rows=int(input("Enter Number of Rows ->   "))
count=0
if(user_input==1):
    while(rows>count):
        print("*"* count, "\n")
        count+=1
if(user_input==0):
    count=rows
    print(count)
    while(count!=0):
        print("*"*count,end="\n")
        count-=1
     """
        