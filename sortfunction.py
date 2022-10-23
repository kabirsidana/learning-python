def func(x):
    return x[1] 
cars=["tata","kia","tesla","bmw","mahindra","jeep"]
# cars.sort(reverse=False)
cars.sort(key=func)
print(cars)

# Questions - make this by using lambda function
#passing lambda in key
#how function sort this (on what basis ) def func(x)