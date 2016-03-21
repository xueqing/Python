#coding = utf-8
import math
import random

##1. hello world
print "hello world!"
print "---END---"

##2. if-else
age = 10
if age > 18:
	print "Adult!"
else:
	print "Teenager"
	print age
print "---END---"

##3. nesting
#score=input("please input the score: ")
score = 10
if score > 60:
	if score > 80:
		print "excellent"
	else:
		print "pass"
else:
	print "fail"
print "---END---"

##4. array
myList = [1, 2, 3, 4, 5.9, "a", 'a', "XYZ", 'ABC']
for ele in myList:
	print ele
print "---END---"

##5. range(start, end, step) function
print range(4)
print range(2, 4)
print range(2, 6, 2)
print "---END---"

##6. math library, list all the primes in [50, 69]
for i in range(50, 70):
	for j in range(2, int(math.sqrt(i)) + 1):
		if i%j == 0:
			break
	else:		# execute this when 'break' isn't executed 
		print i
print "---END---"

##7. random library
print random.random()				# produce random float in [0.0, 1.0)
print random.uniform(10, 20)		# produce random float in [10, 20]
print random.randint(10, 20)		# produce random int in [10, 20]
print random.randrange(10, 20, 2)	# produce random number in range(10,20,2)
print random.choice([1, 2, 3, 4])	# produce random number in sequence[1,2,3,4]
print random.choice("Great Wall!")

myList=[1, 4, 7, 2, 5, 8]
random.shuffle(myList)
print myList
print random.sample(myList, 3)
print "---END---"