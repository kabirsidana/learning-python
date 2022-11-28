# Inverse Pyramid
#*****
#****
#***
#**
#*
rows=int(input("Enter Number of Rows -: "))
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end="")
    print()