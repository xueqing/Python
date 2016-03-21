import re
m = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print m.group()

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group()
print m.group(1)
print m.group(2)

print re.split(r'\s+', 'a b c')

print re.match(r'^(\d+?)(0*)$', '102300').groups()
print re.match(r'^(\d+)(0*)$', '102300').groups()

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) (.*)', line, re.M | re.I)
if matchObj:
	print "matchObj.group() : ", matchObj.group()
	print "matchObj.group(1) : ", matchObj.group(1)
	print "matchObj.group(2) : ", matchObj.group(2)
	print "matchObj.group(2) : ", matchObj.group(3)
else:
	print "No match!!"

	
line = "Cats are smarter than dogs"
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
	print "match-->matchObj.group() : ", matchObj.group()
else:
	print "No match!!"

matchObj = re.search( r'dogs', line, re.M | re.I)
if matchObj:
	print "search-->matchObj.group() : ", matchObj.group()
else:
	print "No match!!"

	
phone = "2004-959-559 # This is Phone Number"
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

num = re.sub(r'\D', "", phone)
print "Phone Num : ", num

print "\n---END---"