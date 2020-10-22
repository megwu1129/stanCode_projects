"""
File: boggle.py
Name: Meg Wu
----------------------------------------
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global
python_set = set()
letter_list = []
boggle_temp_set = set()


def main():
	"""
	This function produces the boggle game.
	"""
	read_dictionary()
	check_format()
	for x in range(len(letter_list)):
		for y in range(len(letter_list)):
			boggle(x, y, '', [])

	print('There are', len(boggle_temp_set), 'words in total.')


def boggle(x, y, current, index):
	global boggle_temp_set
	if current in python_set and len(current) >= 4:
		if current not in boggle_temp_set:
			boggle_temp_set.add(current)
			print('Found: ', current)

	if has_prefix(current):
		for i in range(-1, 2):
			for j in range(-1, 2):
				tem_index = (x+i, y+j)
				if 0 <= y+j < 4 and 0 <= x + i < 4:
					if tem_index in index:
						pass
					else:
						ele = letter_list[y + j][x + i]
						# choose
						current += ele
						index.append(tem_index)
						# explore
						boggle(x+i, y+j, current, index)
						# un-choose
						current = current[:len(current)-1]
						index.pop()


def check_format():
	while True:
		global letter_list
		first_row = input('1 row of letters: ')
		first_row = first_row.lower()
		letter_list1 = first_row.split()
		if first_row[1] != ' ' or first_row[3] != ' ' or first_row[5] != ' ':
			print('Illegal input')
			break
		second_row = input('2 row of letters: ')
		second_row = second_row.lower()
		letter_list2 = second_row.split()
		if second_row[1] != ' ' or second_row[3] != ' ' or second_row[5] != ' ':
			print('Illegal input')
			break
		third_row = input('3 row of letters: ')
		third_row = third_row.lower()
		letter_list3 = third_row.split()
		if third_row[1] != ' ' or third_row[3] != ' ' or third_row[5] != ' ':
			print('Illegal input')
			break
		fourth_row = input('4 row of letters: ')
		fourth_row = fourth_row.lower()
		letter_list4 = fourth_row.split()
		letter_list.append(letter_list1)
		letter_list.append(letter_list2)
		letter_list.append(letter_list3)
		letter_list.append(letter_list4)

		if fourth_row[1] != ' ' or fourth_row[3] != ' ' or fourth_row[5] != ' ':
			print('Illegal input')
			break
		if first_row and second_row and third_row and fourth_row is not None:
			break


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global python_set
	ans = ''
	with open(FILE, 'r') as f:
		for line in f:
			for ch in line:
				if ch != '\n':
					ans += ch
			python_set.add(ans)
			ans = ''


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	prefix_check = False
	for word in python_set:
		if word.startswith(sub_s) is True:
			prefix_check = True
		if prefix_check is True:
			return True
	return False


if __name__ == '__main__':
	main()
