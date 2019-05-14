class MyClass:
"""Bla Bla Bla"""
	def __init__(self, value):
		#define an attribute
		self.attribute = value
		self.new_attribute=self.attribute._some_private_method()
		
	#single underscore is a convention to create a private method
	def _some_private_method(self):
		return a_public_method(self.attribute)
		
		