#this program is about time module 
#which Loop Runs Faster (According to Coding Logic both are same , it depend on pc)
import time
initial=time.time()
a=0
b=0
"""
while a<50:
    print("HELLO")
    a=a+1
result1=time.time()-initial
print(result1)


initial2=time.time()
for b in range(b,50):
    print("Hola")
    b=b+1
result2=time.time()-initial2
print(result2)

if(result1<result2):
    print("While Loop is faster in this case")
elif(result1==result2):
    print("Same speed")
elif(result1>result2):
    print("For Loop is faster in this case")
    """

#printing Local Time
#time.time -> collect time from begining\
#time.localtime -> gives local time
# time.asctime -> It makes time in readable form
#time.sleep(2) -> It will wait 2 second 
localtime=time.asctime(time.localtime(time.time()))
print(localtime)