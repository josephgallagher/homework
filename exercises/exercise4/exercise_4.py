option = 0

while option != '3':
	option = raw_input(\
		"\
		******************************\n\
		EXCERCISE 4 - MENU\n\
		******************************\n\
		1. Write input to file\n\
		2. Write input to screen\n\
		3. Quit\n\
		******************************\n\
		Enter your choice [1-3]: "
		)
	if option == '1':
		write_file = open('file.txt', 'a')
		phrase = raw_input("\t\tEnter a phrase: ")
		write_file.write(phrase + "\n")
		print "\t\tWriting '%s' to file.txt\n" % phrase
		write_file.close()
	elif option == '2':
		phrase = raw_input("\t\tEnter a phrase: ")
		print "\t\t You entered: '%s'\n" % phrase
	else:
		print "\n\t\tThat's not valid input!\n"
		continue
