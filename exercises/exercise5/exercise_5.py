import random
import string
import re


def format(frequency):
    pass

"""
string_file = open('exercise_five.dat', 'w')
for i in range(0, 10):
    random_string = ''.join(
        [random.choice(string.ascii_letters + string.digits) for n in xrange(random.choice(xrange(20)))])
    string_file.write(random_string + "\n")
string_file.close()

string_hash = {}
string_file = open('exercise_five.dat', 'r')
for string in string_file:
    frequency = {char: string.count(char) for char in string.strip()}
    print "\nString:%sFrequency:%s\n" % (string, frequency)
string_file.close()
"""

frequency = {}
punctuation = ["\"", ":", ";", "-", "(", ")", "'s", "s'"]
book_file = open('warandpeace.txt', 'r')
for line in book_file:
	line = line.translate(None, '\"\',.:;()[]{}?!-')
	for word in line.lower().split():
		if (word not in frequency):
			frequency[word] = 1
		else:
			frequency[word] += 1
print frequency
book_file.close()
	

