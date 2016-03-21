##1. declare and create a variable
a = 10
x = y = z = 1
varA, varB, varC = 10, "ABC", [1, 2, 3]
print varA
print varB
print varC

del a, x, varA
#print varA
print "---END---"

##2. global variable
global ABC
ABC = 10
def myTest():
	global ABC
	print ABC
	ABC = 1000
	print ABC
	return ABC

print myTest()
print ABC
print "---END---"