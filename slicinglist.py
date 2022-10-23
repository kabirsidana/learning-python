numbers=[9,3,4,6,5,2,8]
#basic slicing 
print(numbers[:])
#alternative slice
print(numbers[::2])
#reverse with slicing
print(numbers[::-1])
#ending a number at last (append function)
#numbers.append(10)
#print(numbers)
#insert number in list (insert(location,digit))
numbers.insert(0,11)
print(numbers)
#remove a item in list
numbers.remove(6)
print(numbers)
#remove last digit (pop function)
numbers.pop()
print(numbers)
#change a value
numbers[2]=99
print(numbers)