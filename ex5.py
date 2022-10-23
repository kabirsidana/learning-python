#Health Management System of Harry Rohan Aman (codewithharry video 33)
def getdate():
    import datetime
    return datetime.datetime.now()
# def person():
#     name=int(input("1.Harry 2.Rohan 3.Aman  ->  "))
#     return name 
# def lock():
#     work=int(input("1.Diet 2.Exercise  -> "))
#     return work
first=int(input("    1.Log Data    2.Retrieve Data   "))
if first==1:
    work=int(input("1.Diet   2.Exercise  ->  "))
    if work==1:
        name=int(input("1.Harry 2.Rohan 3.Aman ->  "))
        if name==1:
            f=open("harrydiet.txt","a")
            print(f.write("\n"))
            print(f.write(str(getdate())))
            print(f.write(" : "))
            f.write(input("\n Enter Here  -> \n"))
            print("Added Successfully")
            f.close()
        if name==2:
            f=open("rohandiet.txt","a")
            print(f.write("\n"))
            f.write(str(getdate()))
            print(f.write(" : "))
            f.write(input(" \n Enter Here  ->\n "))
            print("Added Successfully")
            f.close()
        if name==3:
            f=open("amandiet.txt","a")
            print(f.write("\n"))
            f.write(str(getdate()))
            print(f.write(" : "))
            f.write(input(" \n Enter Here  -> \n"))
            print("Added Successfully")
            f.close()    
    if work==2:
        name2=int(input("1.Harry 2.Rohan 3.Aman ->  "))
        if name2==1:
            f=open("harryexercise.txt","a")
            print(f.write("\n"))
            f.write(str(getdate()))
            print(f.write(" : "))
            f.write(input("\n Enter Here  -> \n"))
            print("Added Successfully")
            f.close()
        if name2==2:
            f=open("rohanexercise.txt","a")
            print(f.write("\n"))
            f.write(str(getdate()))
            print(f.write(" : "))
            f.write(input(" \n Enter Here  ->\n "))
            print("Added Successfully")
            f.close()
        if name2==3:
            f=open("amanexercise.txt","a")
            print(f.write("\n"))
            f.write(str(getdate()))
            print(f.write(" : "))
            f.write(input(" \n Enter Here  -> \n"))
            print("Added Successfully")
            f.close()    
elif first==2:
    works=int(input("1.Diet 2.Exercise  ->  ")) 
    if works==1:
        names=int(input("1.Harry 2.Rohan 3.Aman ->  "))  
        if names==1:
            with open ("harrydiet.txt") as f:
                print(f.readlines())
        elif names==2:
            with open ("rohandiet.txt") as f:
                print(f.readlines())        
        elif names==3:
            with open ("amandiet.txt") as f:  
                print(f.readlines())
    if works==2:
        names=int(input("1.Harry 2.Rohan 3.Aman ->  "))  
        if names==1:
            with open ("harryexercise.txt") as f:
                print(f.readlines())
        elif names==2:
            with open ("rohanexercise.txt") as f:
                print(f.readlines())        
        elif names==3:
            with open ("amanexercise.txt") as f:  
                print(f.readlines())
                    