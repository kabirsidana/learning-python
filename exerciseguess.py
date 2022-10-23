# take number ,then take inputs from users
# and check if it  is right or wrong
# and print it is smaller or larger than the answer
# the user will get only limited guess
print("Welcome To the Guess Game ")
print("You Only Have 5 Guesses")
a=12
count=1
for c in range(1,6):
    print("Chance NO. ->",count)
    b=int(input( "Enter The Number ->  "))
    if(a>b):
        print("Smaller")
    elif(a<b): 
        print("Bigger")
    elif(a==b):
        print("!!!! ---YOU WON--- !!!!")
        break
    count=count+1
    print("You Lost The Game")
 


#METHOD 2
"""
#guess a number , 54
count=1
while(count<5):
    user_input=int(input(" Enter the number here "))
    print(" Guess No. ",count)
    if(user_input>54):
        print("Greater")
        count+=1
    elif(user_input<54):
        print("Lesser")
        count+=1
    elif(user_input==54):
        print("YOU WON YOUR GUESS WAS RIGHT")
        break
    print("you lost the game")
"""