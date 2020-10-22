"""
File: largest_digit.py
Name: Meg Wu
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

max_num = 0


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the number that waiting to be compared
	:return: int, return the largest digit in the input number
	"""
	global max_num
	max_num = 0
	return find_largest_digit_helper(n)


def find_largest_digit_helper(n):
	global max_num
	if n < 0:
		n = -n
	if n == 0:
		return max_num
	else:
		temp_max = n % 10
		if temp_max > max_num:
			max_num = temp_max
		return find_largest_digit_helper(n//10)




if __name__ == '__main__':
	main()
