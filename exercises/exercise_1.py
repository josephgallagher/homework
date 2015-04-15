def compute(num1, num2):
	print "The sum of %d and %d is: %d" % (num1, num2, num1 + num2)
	print "The difference of %d and %d is: %d" % (num1, num2, num1 - num2)
	print "The product of %d and %d is: %d" % (num1, num2, num1 * num2)
	print "The quotient of %d and %d is: %d with remainder: %d" % (num1, num2, num1 / num2, num1 % num2 )



def main():
	while True:
		try:
			num1 = long(raw_input("Please enter an INTEGER: "))
			break
		except ValueError:
			continue
	
	while True:
		try:
			num2 = long(raw_input("Please enter an INTEGER not equal to zero: "))
			if (num2 == 0L): 
				continue
			else:
				break
		except ValueError:
			continue
	
	compute(num1, num2)



main()



