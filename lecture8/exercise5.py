# Modify the program below to work from the command line by using argparse. The program should
# take the number x (see code below) as a required argument.
import argparse

def is_perfect(x):
	"""Checks if an integer x is perfect. That is
	if the sum of divisors to x is equal to x.
	Example of a perfect number is 6, because
	1, 2, and 3 divides 6 and 1+2+3=6.
	Parameters:
	x (int): input number
	Returns:
	bool: True if x is perfect
	"""
	sum = 0
	for i in range(1, x):
		if(x % i == 0):
			sum = sum + i
	if sum == x:
		return True
	else:
		return False

def is_prime(x):
	"""Checks if an integer x is a prime number. That is
	if x is only divisible with 1 and itself.
	Parameters:
	x (int): input number
	Returns:
	bool: True if x is a prime number
	"""
	if x >= 2:
		for y in range(2, x):
			if not (x % y):
				return False
	else:
		return False
	return True


def main(args):
	for n in args.x:		
		print(f"The number {n} is prime: {is_prime(n)}")
		print(f"The number {n} is perfect: {is_perfect(n)}")

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Check if a number is prime or perfect."
								  , formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('x', type=int, nargs="+", help='Number to analyze')
	args = parser.parse_args()
	main(args)
