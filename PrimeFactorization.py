factors = []
x = 1234567890
i = 2
while x > 1:
	if x % i == 0:
		x = x/i
		factors.append(i)
	else:
		i = i+1
		
print(factors)
