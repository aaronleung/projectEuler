# making this slightly more generic by storing these as variables
# alternatively we could save these in a separate setting file or ask at runtime
limit = 1000
val1 = 3
sum1 = 0
val2 = 5
sum2 = 0
list = []
newlist = []

while sum1 < limit:
	list.append(sum1)
	sum1 += val1

while sum2 < limit:
	list.append(sum2)
	sum2 += val2
	
for x in list:
	if x not in newlist:
		newlist.append(x)
		
print sum(newlist)