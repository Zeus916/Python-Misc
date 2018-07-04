class Pens:
	def __init__(self, make, penheight, penweight):
		self.make = make
		self.penheight = penheight
		self.penweight = penweight

	def pendetails(self):
		return 'Make: {}, Height: {}, Weight: {}'.format(self.make, self.penheight, self.penweight)

	def penArea(self):
		return (self.penweight * self.penheight) 


pen1 = Pens('Reynolds', 4 , 5)
print(pen1.pendetails())
print(Pens.pendetails(pen1))
print(Pens.penArea(pen1))
pen2 = Pens('Parker', 9, 20)
print(pen2.pendetails())
