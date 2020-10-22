"""
File: anagram.py
Name: Meg Wu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global
python_list = []
anagrams_temp_list = []


def main():
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        else:
            read_dictionary()
            find_anagrams(word)
            print(len(anagrams_temp_list), 'anagrams:', anagrams_temp_list)


def read_dictionary():
    """
    This function reads file "dictionary.txt" and appends words into a Python list
    """
    global python_list

    with open(FILE, 'r') as f:
        for line in f:
            ans = ''
            for ch in line:
                if ch != '\n':
                    ans += ch
            python_list.append(ans)


def find_anagrams(s):
    """
    :param s: str, the word that waiting to be searched
    """
    find_anagrams_helper(s, '', [], '')


def find_anagrams_helper(s, chosen, anagrams_list, index):
    global anagrams_temp_list
    if len(chosen) == len(s):
        if chosen in python_list:
            if chosen not in anagrams_list:
                anagrams_list.append(chosen)
                print('Searching... ')
                print('Found: ', chosen)
            anagrams_temp_list = anagrams_list
    else:
        for i in range(len(s)):
            tem_index = i
            ele = s[i]
            if str(tem_index) in index:
                pass
            else:
                chosen += ele
                index += str(tem_index)
                if has_prefix(chosen) is True:
                    find_anagrams_helper(s, chosen, anagrams_list, index)
                    chosen = chosen[:len(chosen)-1]
                    index = index[:len(index)-1]
                else:
                    chosen = chosen[:len(chosen) - 1]
                    index = index[:len(index) - 1]


def has_prefix(sub_s):
    """
    :param sub_s:(str) A string that stores in chosen
    :return: (bool) return bool if there's a word which starts with sub_s in Python_list
    """
    prefix_check = False
    for word in python_list:
        if word.startswith(sub_s) is True:
            prefix_check = True
        if prefix_check is True:
            return True


if __name__ == '__main__':
    main()
