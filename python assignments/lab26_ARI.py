'''

LAB26:

Compute the ARI for a given body of text loaded in from a file.
The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. T
he general formula to compute the ARI is as follows:

The score is computed by multiplying the number of characters divided by the number of words by 4.71,
adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43.
If the result is a decimal, always round up.

'''

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


def open_book(book):
    with open(book) as file:
        book = file.read().lower().replace('?', '.').replace('!', '.').strip().replace('\n', ' ')
    return book


def count_sentences(book):
    sentences = book.split('.')
    return len(sentences)


def count_words(book):
    words = book.replace('.', ' ').split( )
    return len(words)


def count_characters(book):
    characters = book.replace('.', '').replace(' ', '').replace('\n', '').replace('-', '')
    count = 0
    for c in characters:
        count += 1
    return count


def automated_readability_index(filename):
    book = open_book(filename)
    sentences = count_sentences(book)
    words = count_words(book)
    characters = count_characters(book)
    index = (4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43
    return round(index, 0)

filename = input("Type in the filename of a book > ")

ARI = int(automated_readability_index(filename))
print(f"The ARI for {filename} is {ARI}.")
print(f"This corresponds to a {ari_scale[ARI]['grade_level']} level of difficulty \nthat is suitable for an average person that is {ari_scale[ARI]['ages']} years old.")


# ari_level = ari_scale[ARI]
# print(ari_level['ages'])
# print(ari_level['grade_level'])


# war_of_the_worlds_lab25.txt