limit = 4000000
fib = [1,2]
list = [2]
x = 3

while (x < limit):
	fib.append(x)
	if not 1 & x:
		list.append(x)
	x = fib[-2] + fib[-1]
	
print fib
print list
print sum(list)
