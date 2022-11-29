# 180 Degree Rotated Inverted Half Pyramid 
#    *
#   **
#  ***
# ****
rows= int(input("Enter Number of Rows -: "))
for i in range(rows+1):
    # space = rows-i 
    for s in range(rows-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()