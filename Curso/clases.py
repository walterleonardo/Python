class myrouter(object):
	'''this is a class'''
	def __init__(self, routername, model, serialno, ios):
		self.routername = routername
		self.model = model
		self.serialno = serialno
		self.ios = ios
	def print_router(self, manuf_date):
		print" the router name is:", self.routername
		print" the router model is:", self.model
		print" the router serial is:", self.serialno
		print" the router ios is:", self.ios
		print" the router model and date is:", self.model + manuf_date
		

router1 = myrouter("R1","2600","123","12.4")

print router1.model
print router1.ios

router1.print_router("02150101")


router2 = myrouter("R2","2100","456","11.4")

router2.print_router("20150202")


print getattr(router2,"ios")
setattr(router2, "ios", "10.4")
print getattr(router2,"ios")

print hasattr(router2, "ios")

delattr(router2, "ios")

print hasattr(router2, "ios")

print "verificamos si existe ls instancia dentro de la clase"
print isinstance(router2, myrouter)


class mynewrouter(myrouter):
	def __init__(self, routername, model, serialno, ios, portsno):
		myrouter.__init__(self, routername, model, serialno, ios)
		self.portsno = portsno
	def print_new_router(self, string):
		print string + self.model

new_router1 = mynewrouter("newr1","1800","111111","12.2","10")

print new_router1.portsno

new_router1.print_router("asdasdasdasd")


new_router1.print_new_router("asdasdasdasd")