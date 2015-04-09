def convert(gal):
	gallons = str(gal)
	litres = gal * 3.7854 
	barrels = gal / 19.5
	pounds = gal * 20
	ethanol = (115000.0/75700.0) * gal
	cost = gal * 4
	print "Original number of gallons is: %f" % gal
	print gallons + " gallons is the equivalent of %f litres." % litres
	print gallons + " gallons of gasoline requires  %f barrels of oil." % barrels
	print gallons + " gallons of gasoline produces %f pounds of CO2." % pounds
	print gallons + " gallons of gasoline is energy equivalent to %f gallons of ethanol." % ethanol
	print gallons + " gallons of gasoline requires %f US dollars." % cost


def main():
	while True:
		try:
			gal = float(raw_input("Please enter the number of gallons of gasoline: "))
			break
		except ValueError:
			continue
	convert(gal)


main()

