a=77
x=12 #global variable
#function finds x locally if they fail to find they will go to global
def function():
    x=55
    print(x)
function()
#It will throw error if we want to increment to global variable
#def function2():
#    a=a+33
#    print(a)
#function2()

#thats why we need global keyword
def function3():
    global a
    a=a+23
    print(a)
function3()