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


# Checking Prime Number with class and object
'''
class Prime:
    def __init__(self,num):
        self.num=num
    def process(self):
        temp=self.num
        a=0
        for i in range(1,self.num):
            if((temp%i)==0):
                print(" Not a Prime Number")
                break
        else:
            print("Prime")    

ob=Prime(12)
ob.process()
        '''


# Prime Number between 1-100
'''
for n in range(5,300+1):

    for i in range(2,n):
        if(n%i==0):
            break
    else:
        print(n)       
'''
