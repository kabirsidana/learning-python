# Half Pyramid / Straight Pyramid
#* 
#**
#***
#****
#*****
#******
rows=int(input("Enter Rows -: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print()        