age=int(input("Enter your age -: "))
if age in range(7,90):
    if(age==18):
        print("come for interview")
    elif(age>18):
        print("yes you can")
    else:
        print("sorry you cannot ")
else:
    print("invalid Age ")        