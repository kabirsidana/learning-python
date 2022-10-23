#giving name to a string 
mystring="Kabir is my name"
print(mystring)
#Printing only some letter in a string
print(mystring[4])
#printing a Series of elements
print (mystring[0:6]) #it exclude 7th digit it is 0-6 letter
#finding the length of string
print(len(mystring))
#if we dont put ending 
print(mystring[0:]) #it will print the whole
#print alternative letters
print(mystring[0:6:2])
#print without initial value
print(mystring[:6])#it will automatically take it as zero
#negitive value
print(mystring[-5:-1]) #it will go in reverse 
#how to reverse a string
print(mystring[::-1])
#print alternative reverse of string
print(mystring[::-2])