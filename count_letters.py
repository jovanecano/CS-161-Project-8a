# Author: Jovane Cano
# GitHub username: jovanecano
# Date: 05/22/2024
# Description:
"""This script will create a function called count_letters that will count and return the number of times a letter
        appears in the string while ignoring case sensitivity"""


def count_letters(string):
    """as noted above this function will count the letters withing the given string, while ignoring case sensitivity"""
    letters_counted = {}  # empty dictionary to store the count of letters

    for char in string:  # this for loop will iterate through all the characters in the given string
        if "a" <= char <= "z" or "A" <= char <= "Z":#first checks if what is being iterated is a letter
            upper_case = char.upper()
            if upper_case in letters_counted:
                # adds 1 to count if the letter was already counted, else starts count
                letters_counted[upper_case] += 1
            else:
                letters_counted[upper_case] = 1
    return letters_counted


# testing function using the longest word in the english language: pneumonoultramicroscopicsilicovolcanoconiosis
# print(count_letters("pneumonoultramicroscopicsilicovolcanoconiosis"))
# output is: {'P': 2, 'N': 4, 'E': 1, 'U': 2, 'M': 2, 'O': 9, 'L': 3, 'T': 1, 'R': 2, 'A': 2, 'I': 6, 'C': 6, 'S': 4, 'V': 1}