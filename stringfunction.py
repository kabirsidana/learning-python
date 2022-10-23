mystring="how are you all"
# function isalnum() , it checks if all are alphabet and numeric 
#false because it is contain spaces
print(mystring.isalnum()) 
#check only alphabets isalpha() , it check only alphabets , spaces are not allowed
print(mystring.isalpha())
#to Check ending word or letter , endswith()
print(mystring.endswith("all"))
# To count occurance of a variable
print(mystring.count("a"))
#Function to capitalize first letter
print(mystring.capitalize())
#find a place of a word
print(mystring.find("you"))
# Replace string to lower characters (no capital letters)
print(mystring.lower())
# Replace string to upper characters (all capital)
print(mystring.upper())
#Replace a word to another word
print(mystring.replace("are","is"))