num = float(input("Please enter your starting number: "))

def is_hot(x):
	if x < 2:
		return -1
	else:
		x1 = x -1
		x2 = x/2
		return is_hot(x1) * is_hot(x2)
			
if is_hot(num) < 0:
	print("hot")
else:
	print("cold")
