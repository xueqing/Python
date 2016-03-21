def Div(first, second = 1):
	return first / second
print Div(4, 2)
print Div(second = 2, first = 4)
print Div(4)

def Sum(*varTuple):
	sum = 0
	for x in varTuple:
		sum += x
	return sum
print Sum(10, 20, 30)

def Run(State, *varTuple):
	if State == '+':
		rtnVal = 0
		for x in varTuple:
			rtnVal += x
	if State == '*':
		rtnVal = 1
		for x in varTuple:
			rtnVal *= x
	return rtnVal
print Run('*', 10, 20, 30)
print Run('+', 10, 20, 30)

def Test(inVal):
	inVal = 100
	return inVal
a = 10
print Test(a)
print a

def TestList(inList):
	inList.append(99)
	print inList
	return;
myList = [1, 2, 3, 4]
TestList(myList)
print myList

myLambda = lambda x, y : x + y
print myLambda(10, 20)
print myLambda(20, 30)
print map(lambda x : x * x, [1, 2, 3, 4])

print "---END---"