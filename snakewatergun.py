#Snake Water Gun Game
#Snake vs Water - Snake Wins
#Snake vs gun - Guns wins
#gun vs Water - Water wins
#user vs computer (Total 10 Rounds)
print("---THIS IS SNAKE WATER GAME ---")
import random
userpoints=0
computerpoints=0
tie=0
for round_number in range(1,11):

    d=["snake","water","gun"]
    a=random.choice(d)
    b=input(" snake , water , gun  -> ")
    print("----- ROUND NUMBER ----- ",round_number )
    if(a==b):
        tie=tie+1
        print("Computer ->",a)
        print("TIE",)
    elif(a=="snake" and b=="water" ): 
        print("Computer ->",a)
        computerpoints=computerpoints+1
        print("Computer Wins")
    elif(a=="water" and b=="snake"):
        print("Computer ->",a)
        userpoints=userpoints+1
        print("User Wins")
    elif(a=="gun"and b=="water"):
        print("Computer ->",a)
        userpoints=userpoints+1
        print("User Wins")
    elif(a=="water" and b=="gun"):
        print("Computer ->",a)
        computerpoints=computerpoints+1
        print("Computer Wins")
    elif(a=="snake" and b=="gun"):
        userpoints=userpoints+1
        print("User Wins")
    elif(a=="gun " and b=="snake"):
        print("Computer ->",a)
        computerpoints=computerpoints+1
        print("Computer Wins")
print("Computer Points Are ",computerpoints)
print("User Points Are ",userpoints)
print("NUmber of Tie Round ",tie)
if(userpoints>computerpoints):
    print("  USER WON  ") 
elif(userpoints<computerpoints):
    print("  COMPUTER WON ")  
elif(userpoints==computerpoints):
    print("The Match is Tie Let Play Again")    