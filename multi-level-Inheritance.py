#Multilevel Inheritance
class Revolutionary_war:
    duration="1775 to 1783"
    def __init__(self):
        print("Revolutionary War")
class World_War_1(Revolutionary_war):
    end_date=1919
    def __init__(self):
        print("world war 1")

class World_War_2(World_War_1):
    start_date=1939
    def __init__(self):
        print("world war 2")

# kabir=World_War_1()
kabir=World_War_2()
print(kabir.duration)