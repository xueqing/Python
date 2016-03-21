class UD:
	udCount = 0
	def __init__(self, U, D):
		UD.udCount += 1
		self.Up = U
		self.Down = D
	def __add__(self, valR):
		return UD(self.Up*valR.Down + self.Down*valR.Up, self.Down*valR.Down)
		
	def __str__(self):
		return str(self.Up) + '/' + str(self.Down)
	
	def __cmp__(self, valR):
		return self.Up*valR.Down == self.Down*valR.Up

	def __eq__(self, valR):
		return self.Up*valR.Down == self.Down*valR.Up

	def display(self):
		print "%d %d" %(self.Up, self.Down)
		
	def __del__(self):
		print "_del_Dying!"

udA = UD(1, 2)
udB = UD(2, 3)

udA.display() 

print UD.udCount

udC = udA + udB
udC.display()
print UD.udCount

print str(udC)
repr(udC)

print cmp(udA, UD(2, 4))
print udA == UD(2, 4)

print "\n---END---\n"