#Simple reading the file
"""
f=open("kabir.txt","r")
print(f.read())
"""
#Writing in file / write destroy all data and add new data 
"""
f1=open("kabir.txt","w")
f1.write("zebra")
""" 
#appending data/ append does not delete prevoius data it adds to existing data
"""
f2=open("kabir.txt","a")
f2.write(" lion")
"""
# Read and read and write(appends) both
"""
f3=open("kabir.txt","r+")
print(f3.read())
f3.write("this is r+ mode")
"""