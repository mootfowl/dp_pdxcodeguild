'''

LAB25: v2

Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.


'''

with open('war_of_the_worlds_lab25.txt') as f:
    contents = f.read()

x = contents.lower().replace('.', '').replace('?', '').replace('-', ' ').replace(',', '').replace('  ', ' ').replace(':', ' ')
individual_words = x.split() # Converts the string to a list of words
word_pairs = []

for word in range(len(individual_words) - 1):
    word_pairs.append(individual_words[word] + ' ' + individual_words[word +1])

print(word_pairs)


word_pair_count = {}

for pair in word_pairs:
    if pair in word_pair_count: # Checks if each word pair is already in the dictionary...
        word_pair_count[pair] += 1 # ...if it is, it updates the word's value by 1
    else:
        word_pair_count.update({pair: 1}) # If it's not in the dictionary, it creates a new key value pair

print(word_pair_count)

pairs = list(word_pair_count.items()) # list of tuples
print(pairs)
pairs.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(pairs))):  # print the top 10 words, or all of them, whichever is smaller
    print(pairs[i])