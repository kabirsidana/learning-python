# Solid Rectangle Pattern
# *  *  *  *  *    
# *  *  *  *  *  
# *  *  *  *  *  
rows=int(input("Enter Number of Rows -: "))
column=int(input("Enter Number of Columns -: "))
for i in range(rows):
    for j in range(column):
        print(" * ",end="")
    print()