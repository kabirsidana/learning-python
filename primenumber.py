print("-----Program to Check If it is Prime Or Not------")
p=int(input("Enter The Number  -> "))
for i in range(2,p):
    if (p%i)==0:
        print("not a prime Number")
        break
#we will use else with for Loop not with if statement
#beacuse it will print it is prime Multiple times
#so we will remove space before else and use it directly under for loop
else:
    print("it is a Prime Number")

print("end")