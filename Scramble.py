def interleave(str1, str2):
	return "".join(i for j in zip(str1,str2) for i in j)

def scramble(x):
	if len(x) == 1:
		return x
	else:
		s1 = scramble(x[:int(len(x)/2)])
		s2 = scramble(x[int(len(x)/2):])
		return  interleave(s1,s2) 

##print(scramble("Madam I'm Adam. "))

##print(scramble("We demand rigidly defined areas of doubt and uncertainty!       "))

result = (scramble("The illusion of self-awareness. Happy automatons, running on trivial programs. I'll bet you never guess. From the inside, how can you?" + " " * 122))

#message = scramble("This is a message")
#print(message)

#print(scramble(message))

#print(scramble(scramble("12345678")))

fileHandler = open("output.txt", "w")
fileHandler.write(result)

