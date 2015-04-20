def catch_inside(in_file):
	try:
		f = open(in_file, "r")
		for line in f:
			print line.split()
	except IOError:
		print "Error: Cannot find the input file to 'catch_inside' function!"


def catch_outside(in_file):
	f = open(in_file, "r")
	for line in f:
		print line.split()


def main():
	passed_file = "in_file"
	catch_inside(passed_file)
	try:
		catch_outside(passed_file)
	except IOError:
		print "Error: Cannot find the inut file to 'catch_outside' function!"


if __name__ == "__main__":
	main()

