##1.string
strA = "ABCDEFG"
print strA[2 : 4]
print strA[2 :]
print strA[: 4]
print strA[-5 : -3]
print strA[-5 :]
print strA[: -3]
print "---END---"

##2. list
myList = [1, 2, "XYZ", [1, 2, 4], True]
print myList
print myList[1], myList[-1]
myList[-1] = False

print len(myList)

myList.append(12)
myList.insert(1, "ABC")
print myList

myList.pop()
myList.pop(2)
print myList

hisList = []
print len(hisList)
print "---END---"

##3. create a list
listA = range(0, 5)
print listA

listB = []
for i in range(0, 5):
	listB.append(i * i)
print listB

listC = [i*i for i in range(0, 5)]
print listC

listD = [i*i for i in range(0, 5) if i%2 == 0]
print listD

listE = [str(i) + "*" + str(j) + "=" + str(i*j) for i in range(1, 5) for j in range(6, 10)]
print listE
print "---END---"

##4. functions abut list
def OP(x):
	return x * x
listA = map(OP, [1, 2, 3, 4])
print listA

def ADD(x, y):
	return x + y
listB = reduce(ADD, [1, 2, 3, 4])
print listB

def isEven(x):
	return x % 2 == 0
listC = filter(isEven, [1, 2, 3, 4])
print listC
listD = filter(isEven, range(1, 5))
print listD

listE = sorted([1, 3, 5, 2, 4, 6, 8])
print listE

def  reverseSort(x, y):
	if x > y:
		return -1
	else:
		return 1
	return 0
listF = sorted([1, 3, 5, 2, 4, 6, 8], reverseSort)
print listF
print "---END---"

##5. tuple
myTuple = ('abcd', 76, 2.3, 'john', 70.2)
hisTuple = (123, 'john')
print myTuple
print myTuple[0]
print myTuple[1 : 3]
print myTuple[2 :]
print hisTuple * 2
print hisTuple + myTuple
#myTurple[1] = 80
print "---END---"

##6. dictionary
myDic = {'name' : 'john', 'code' : '654', 'dept' : 'sales'}
hisDic = {}
hisDic['one'] = "this is one"
hisDic[2] = "this is two"
print myDic["name"]
print hisDic["one"]
print hisDic
print hisDic.keys()
print hisDic.values()

myDic.pop("code")
print myDic
print "name" in myDic
print myDic.get("name")
print myDic.get("code")
print myDic.get("code", True)
print "---END---"

##7. set
mySet = set([1, 2, 3])
hisSet = set([2, 3, 4])
mySet.add(4)
hisSet.remove(2)
print mySet, hisSet
print mySet & hisSet
print mySet | hisSet
wordSet = set(["Apple", "IBM", "Lenovo", "HuaWei", "Tencent"])
print wordSet
print "---END---"