# super() function provides us the facility to refer to the parent class explicitly.
class Human:
    def __init__(self):
        self.talk = "Humans have ability to talk"
        self.see = "Humans has ability to see things with eyes"


class Indian(Human):
    def __init__(self):
        super().__init__()
        self.talk = "Indian People Talk in Hindi Tamil etc "


ob = Indian()
print(ob.talk)

# this will not work without super()
print(ob.see)
