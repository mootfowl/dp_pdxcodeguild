'''
LAB19 - Palindrome and Anagram

PALINDROME:

A palindrome is a word that's the same forwards or backwards, e.g. racecar.
Another way to think of it is as a word that's equal to its own reverse.
Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

ANAGRAM:

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.
Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother,
False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal

'''

def check_palindrome(word):
    reversed = ((word[::-1]).lower()) # reverses the string
    return reversed == word.lower() # boolean check


prompt = input("Enter a word to check if it is a palindrome. > ")
print(check_palindrome(prompt))


def check_anagram(word1, word2):
    word1_list = list((word1.lower()).replace(' ', ''))
    word1_list.sort()
    word2_list = list((word2.lower()).replace(' ', ''))
    word2_list.sort()
    return word1_list == word2_list


promptA = input("Enter the first word. > ").lower()
promptB = input("Enter the second word. > ")
print(check_anagram(promptA, promptB))
