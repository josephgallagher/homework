lightspeed = 299792458.0

def barleycorns_per_day(speed):
	return speed*(24.0)*(117.647)*(1609.34) #ie: x(mi/hr) * 24(hr/day) * 117.647(barleys/meter) * 1609.34(meter/mi) = y(barleys/day)
def furlongs_per_fortnight(speed):
	return speed*(24.0)*(14.0)*(1760.0)/(220.0) #ie:  x(mi/hr) * 24(hr/day) * 1(furlong/220yd) * 1760(yd/mi) * 14(days/fortnight) = y(furlong/fortnight)
def mach_number(speed):
	return speed/(761.207051) #ie: speed of sound is 761.207051 
def percentage_of_lightspeed(speed):
	return (speed*(1609.34)/(3600))/lightspeed #ie: ( x(mi/hr) * (1609.34meter/mi) * 1(hr/3600s) ) / lightspeed(meter/s)



def main():
	while True:
		try:
			speed = float(raw_input("Please enter a speed in miles/hour: "))
			break
		except ValueError:
			continue
	print barleycorns_per_day(speed)
	print furlongs_per_fortnight(speed)
	print mach_number(speed)
	print percentage_of_lightspeed(speed)

main()

