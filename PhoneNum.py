reply = input('Enter your phone number separated by spaces ')
numbers = [int(n) for n in reply.split()]
x = reply.replace(" ", "")
x = int(x)

mySum = sum(numbers)
y = x - mySum
y = str(y)

while len(y) > 1:
	numbers = [int(i) for i in y]
	mySum = sum(numbers)
	y = str(mySum)
	
print(y)
