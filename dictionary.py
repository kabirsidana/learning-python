# dictionary is key value pair 
#it is used by Curly braces {}
food={"rohan":"milk", "rahul":"roti","harry":"juice"}
print(food)
#printing someone food or Value pair
print(food["harry"])
#value can be list or any other dictionary, dictionary in dictionary
diet={"shub":{"m":"roti","L":"rice","D":"salad"}}
print(diet["shub"])
#printing lunch of shub
print(diet["shub"]["L"])
#adding in dictionary
food["ankit"]="bread"
print(food)
#deleting from library
del food["rahul"]
print(food)
#printing keys
print(food.keys())
#printing items
print(food.items())