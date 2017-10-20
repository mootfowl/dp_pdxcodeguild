'''

LAB27: Contact List v1

Let's build a program to manage a list of contacts.
To start, we'll build a CSV ('comma separated values') together, and go over how to load that file.
Headers might consist of name, favorite fruit, favorite color, catch phrase.
Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.

'''

with open('lab27_contacts.csv', 'r') as file:
    contents = file.readlines()
key = contents.pop(0).replace('\n', '').split(',') # Cleans up the file with replace, and stores the first line as a list "key"
contact_list = []

for line in contents: # At this point, contents now only has each entry since the key was popped off.
    temp = line.replace('\n', '').split(',') # Cycles through each line
    # print(temp)
    contact = {}
    for i in range(len(key)): # Cycles through each value and pairs it with the corresponding key element
        dict = {key[i]: temp[i]}
        contact.update(dict)
    contact_list.append(contact)

# print(contents)
# print(key[0])
print(contact_list)