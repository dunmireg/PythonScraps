reply = input('Enter your postfix expression to be evaluated ')
exp = [n for n in reply.split()]

stack = []

for i in exp:
	if i == "+":
		temp2 = stack.pop()
		temp1 = stack.pop()
		stack.append(temp1+temp2)
	elif i == "-":
		temp2 = stack.pop()
		temp1 = stack.pop()
		stack.append(temp1-temp2)
	elif i == "*":
		temp2 = stack.pop()
		temp1 = stack.pop()
		stack.append(temp1*temp2)
	elif i == "/":
		temp2 = stack.pop()
		temp1 = stack.pop()
		stack.append(temp1/temp2)
	else:
		stack.append(int(i))

print(stack)
