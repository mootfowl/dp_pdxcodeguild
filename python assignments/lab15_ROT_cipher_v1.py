'''
LAB15: Write a program that decrypts a message encoded with ROT13 on each character starting with 'a',
and displays it to the user in the terminal.
'''

# DP note to self: if a = 1, ROT13 a = n (ie, 13 letters after a)
# First, let's create a function that encrypts a word with ROT13...

alphabet = 'abcdefghijklmnopqrstuvwxyz '
key = 'nopqrstuvwxyzabcdefghijklm '

def encrypt(word):
    encrypted = ''
    for letter in word:
        index = alphabet.find(letter) # returns the alphabet index of the corresponding letter
        encrypted += (key[index]) # prints the rot13 letter that correlates to the alphabet index
    return encrypted

def decrypt(encrypted_word):
    decrypted = ''
    for letter in encrypted_word:
        index = key.find(letter)
        decrypted += (alphabet[index])
    return decrypted


secret_sauce = input("Type in a word > ")
print(encrypt(secret_sauce))

not_so_secret_sauce = input("Type in an encrypted word > ")
print(decrypt(not_so_secret_sauce))
