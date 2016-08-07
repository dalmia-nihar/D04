#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

def take_input():
	try:
		num = int(input("Please enter an integer between 1 to 25: "))
		return num
	except: 
		print("Nice Try, not an integer")
			


def check_random(x):
	for i in range(5):
		print("Chance: " + str(i+1))
		n = take_input()
		if n == None:
			continue
		elif x == n:
			print ("Bingo!")
			break
		elif 1 <= n <= 25 and x < n:
			print ("Too High")
			continue
		elif 1 <= n <= 25 and x > n:
			print ("Too Low")
			continue
		else:
			print("Number not between 1 and 25")


################################################################################
def main():
    x = random.randint(1, 25)
    check_random(x)
    print("The correct answer was: " + str(x))
    print("Thank you for playing!")
 

if __name__ == '__main__':
    main()