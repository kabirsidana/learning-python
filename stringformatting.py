#Using %s ( Where it will find the %s it will put the text there)
"""
me = "KABIR"
subject="python"
line = "this is %s "%me  #it will concatinate
print(line)
line2 = "this is %s!! "%me
print(line2)
line3= "this is %s %s"%(me,subject)
print(line3)

"""
# Using format() function
me="kabir sidana"
address="Rajasthan"
a="HEllO I am {} and i live in {}"
# a="hello i am {0} and i live in {1}"
b=a.format(me,address)
print(b)
