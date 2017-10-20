'''

LAB25: Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and
display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a
word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a
count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts.
'''

with open('war_of_the_worlds_lab25.txt') as f:
    contents = f.read()

x = contents.lower().replace('.', '').replace('?', '').replace('-', ' ').replace(',', '').replace('  ', ' ').replace(':', ' ')
individual_words = x.split() # Converts the string to a list of words

# print(x)

word_count = {}

for word in individual_words:
    if word in word_count: # Checks if each word is already in the dictionary...
        word_count[word] += 1 # ...if it is, it updates the word's value by 1
    else:
        # word_count.update({word: 1}) # If it's not in the dictionary, it creates a new key value pair
        word_count[word] = 1

print(word_count)

words = list(word_count.items()) # list of tuples
print(words)
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])