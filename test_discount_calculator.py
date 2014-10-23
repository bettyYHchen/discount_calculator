import unittest
from discount_calculator import calculate_discount

class DiscountCalculatorTests(unittest.TestCase):
	# the basic case provided by the example
	def testBasicCase(self):
		pay = calculate_discount(200.0,10.0,30.0)
		self.assertEqual(pay,150.0)

	# if there is only relative discount
	def testNoAbsDiscount(self):
		pay = calculate_discount(200.0,10.0,0)
		self.assertEqual(pay,180.0)

	# if there is only absolute discount
	def testNoRelativeDiscount(self):
		pay = calculate_discount(200.0,0,30.0)
		pay = round(pay,3)
		self.assertEqual(pay,170.0)

	# if there is no discount
	def testNoDiscount(self):
		pay = calculate_discount(200.0,0,0)
		pay = round(pay,3)
		self.assertEqual(pay,200.0)

	# if price  after relative discount is less than the absolute discount
	def testPricelessthanAbsDis(self):
		with self.assertRaises(ValueError):
			pay = calculate_discount(10.0,10.0,30.0)
	# if inputs are of type other than floats and zeros
	def testWrongType(self):
		with self.assertRaises(ValueError):
			pay = calculate_discount("10",30,0)
	# if the raltive discount is negative
	def testNegRelative(self):
		pay = calculate_discount(200.0,-10.0,20.0)
		pay = round(pay,3)
		self.assertEqual(pay,200.0)
	# if the absolute discount is negaitve
	def testNegAbsolute(self):
		pay = calculate_discount(200.0,10.0,-30.0)
		pay = round(pay,3)
		self.assertEqual(pay,210.0)

suite = unittest.TestLoader().loadTestsFromTestCase(DiscountCalculatorTests)
unittest.TextTestRunner(verbosity=2).run(suite)





