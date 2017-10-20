'''
LAB15: v2

Allow the user to input the amount of rotation used in the encryption / decryption.


'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(word, offset):
    encrypted = ''
    for letter in word:
        index = alphabet.find(letter) # Find returns the index (from alphabet) for each letter in word
        ROT = index - offset # ROT subtracts the number they chose from the index number
        encrypted += (alphabet[ROT])
    return encrypted


word = input("Type in a word > ") # The word to be encrypted
secret_sauce = int(input("And now type in a number > ")) # The amount to "rotate"
print(encrypt(word, secret_sauce))

# not_so_secret_sauce = input("Type in an encrypted word > ")
# print(decrypt(not_so_secret_sauce))
