dict = {"beta": 1, "alfa": 2, }

maxkey = ""
maxval = 0

for x in dict:
	print dict[x]
	if dict[x] > maxval:
		print x.title()
		maxkey = x.title()
		maxval = dict[x]

print maxkey, maxval