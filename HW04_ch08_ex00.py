#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports


def count(word,ch):
	cnt = 0
	for letter in word:
		if letter == ch:
			cnt += 1
	print("The count of '" + ch + "' in the string '" + word + "' is: " + str(cnt))

###############################################################################
def main():
    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count("Banana", "a")
    count("Banana", "z")
    count("lol", "l")
    count("University of California, Berkeley", " ")
    count("MIMS", "S")
    count("This is the last one", "s")


    


if __name__ == '__main__':
    main()
