#fibonnaci series by for loop
"""
first=0
print(first)
second=1
print(second)
next=first+second
for i in range(10):
    # print(first,"\n");print(second,"\n")
    first=second
    second=next
    next=first+second
    print(next);
    i+=1
"""

#fibonacci by recurssion
#this method will print the value at index like 10th is 34
"""
def fib(n):
    if(n==1):  #this is base
        return 0
    if(n==2):  #this is base
        return 1
     else:
        return fib(n-1)+fib(n-2) #this is recursive case
print(fib(10))
"""
#fibonnaci series print , using for loop and recursions
def fib(n):
    if(n==1):
        return 0  #base case
    if(n==2):
        return 1  #base case
    else:
        return fib(n-1)+fib(n-2) # Recursive Case
n=int(input(" How long you want the series "))
for i in range(1,n+1):
    print(fib(i))
    
