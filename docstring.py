#docstring is a breif discription of what the function do
# it should be the first line of function , enclosed with 3 quotes  
def area(b,h):
    """ This Function Helps To Calculate the Area of Tringle. """
    a=(1/2)*b*h
    return a

print(area.__doc__)