# class Human():
# 	def __init__(self, name, age):
# 		# self.name = "Mostafa"

# 		# self.age = 26

# 		# self.do_something()

# 		print(name, age)


	# def do_something(self):
	# 	print(self.age)
	# 	print("Mostafa is programming.")


	# def do_math(self, num1=8, num2=6):
	# 	self.result = num1 + num2

	# 	self.do_something()

	# 	print(self.result)




# h1 = Human("Mostafa", 26)

# print(h1.name)

# h1.do_something(3)

# h1.do_math(5, 10)

# print(h1.name)


class A():
	def __init__(self):
		self.name = "Mostafa"

	def do_something(self):
		print(self.name)


class B(A):
	def __init__(self):
		super().__init__()
		self.family = "Lotfi"

	def do_math(self, num1, num2):
		print(num1+num2)


b1 = B()

print(b1.name, b1.family)
