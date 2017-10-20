'''

LAB25: v3
Let the user enter a word, then show the words which most frequently follow it.

'''

with open('war_of_the_worlds_lab25.txt') as f:
    contents = f.read()

x = contents.lower().replace('.', '').replace('?', '').replace('-', ' ').replace(',', '').replace('  ', ' ').replace(':', ' ')
words = x.split() # Converts the string to a list of words

# print(x)

word_count = {}

def what_follows(word):

    if word in words:

print(word_count)

