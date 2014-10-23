def calculate_discount(item_cost, relative_discount, absolute_discount):
	if (type(item_cost) != float) and (item_cost != 0):
		raise ValueError("item_cost must be a float or a zero")
	if (type(relative_discount) != float) and (relative_discount != 0):
		raise ValueError("relative_discount must be a float or a zero")
	if (type(absolute_discount) != float) and (absolute_discount != 0):
		raise ValueError("absolute_discount must be a float or a zero")		

	rdiscount = relative_discount/100.0
	rrate = 1.0-rdiscount
	price1 = item_cost * rrate
	price2 = price1 - absolute_discount
	if price2 < 0:
		raise ValueError("Absolute discount is too large")
	else:
		return price2

def main():
	item_cost = 200.0
	relative_discount = -10.0
	absolute_discount = 20.0
	print "the original price is {:.2f}, after applying the relative discount {:.2f} and\
	the absolute discount {:.2f}, the price is now {:.2f}".format(item_cost,relative_discount\
		,absolute_discount,calculate_discount(item_cost,relative_discount,absolute_discount))

if __name__ == "__main__":
	main()



