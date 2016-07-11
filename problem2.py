# -*- coding: utf-8 -*-
# author: Ricardo Ruiz


# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# (0),(1), 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

from math import sqrt

phi = ( 1 + sqrt(5) ) / 2.0

def fibonacci(n):
	"""Explicit formula for the n position
	of fibonnaci sequence"""
	
	result = int((phi**n - (phi-sqrt(5))**n) / sqrt(5))

	return result

def nearest(limit):
	"""Calculate which is the position of the fibonacci
	numbers whose value is the nearest 4000000"""

	for num in xrange(1000): # Generator

		fib = fibonacci(num)
		if fib > limit:
			return (num - 1)
		elif fib == limit:
			return num


def sum_all_fib_even_numbers(limit=4000000):
	"""Because the sum of two odd numbers is even,
	even numbers are in [3, 6, 9..] positions"""

	last = nearest(limit)
	evens = range(3, last + 1, 3)

	return sum([fibonacci(even) for even in evens])

if __name__ == '__main__':

	solution = sum_all_fib_even_numbers()
	print(solution)