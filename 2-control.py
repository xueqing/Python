import math
import random

##1. if/else/elif
score = input("please input the score: ")
if score > 80:
	print "excellent"
elif score > 70:
	print "good"
elif score > 60:
	print "pass"
else:
	print "fail"
print "---END---"

##2. while
n = 1
sum = 0
while n <= 100:
	sum += n
	n += 1
print sum
print "---END---"

##3. nested while
n = 2
while n <= 100:
	i = 2
	end = int(math.sqrt(n))
	while i <= end:
		if(n%i == 0):
			break;
		i += 1
	else:
		print n
	n += 1
print "---END---"

##4. for-in
for x in [1, 2, 3, 46]:
	print x

for x in range(1, 5):
	print x
	
for x in "anvds":
	print x

for x in random.sample("ajioads", 3):
	print x

print "---END---"