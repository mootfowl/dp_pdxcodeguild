'''

LAB27: Contact List v2

Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

'''

with open('lab27_contacts.csv', 'r') as file:
    contents = file.readlines()
key = contents.pop(0).replace('\n', '').split(',') # Cleans up text and makes a list
contact_list = []
contact_dict = {}

for line in contents:
    temp = line.replace('\n', '').split(',') # Cleans up text and makes a list
    # print(temp)
    contact = {}
    for i in range(len(key)):
        dict = {key[i]: temp[i]} # Creates a mini dictionary of a single key:value pair
        contact.update(dict)
    contact_list.append(contact) # Adds the dictionary to the list

for i in range(len(contact_list)):
    list_entry = {contact_list[i]['name']: contact_list[i]}
    contact_dict.update(list_entry) # Embeds a dictionary within a dictionary {name: {'name': name, 'fav color': etcetera}


# print(contents)
# print(key[0])
# print(contact_list)
# print(contact_dict)

def main_menu():
    selection = input("\nCONTACT LIST - MENU (type one) > view all | create | retrieve | update | delete | exit > ")
    if selection == 'view all':
        print('\n')
        view_all_records()
    elif selection == 'create':
        print('\n')
        create_record()
    elif selection == 'retrieve':
        print('\n')
        retrieve_record()
    elif selection == 'update':
        print('\n')
        update_record()
    elif selection == 'delete':
        print('\n')
        delete_record()
    elif selection == 'exit':
        exit()
    else:
        main_menu()


def view_all_records():
    for person in contact_dict:
        print(contact_dict[person])
    main_menu()


def create_record():
    name = input("What is the new contact's first name? > ")
    color = input("What is their favorite color? > ")
    fruit = input("And most importantly, what is their favorite fruit? > ")
    contact_dict.update({name: {'name': name, 'favorite color': color, 'favorite fruit': fruit}})
    print(f"A new entry for {name} has been created:")
    print(contact_dict[name])
    main_menu()


def glance_list():
    all = []
    for person in contact_dict:
        all.append(person)
        all.sort()
    print(f"CONTACTS: {all}")


def retrieve_record():
    glance_list()
    name = input("Who are you looking for? > ")
    if name in contact_dict:
        print(contact_dict[name])
        main_menu()
    elif name not in contact_dict:
        print(f"There is no one by the name of {name} stored in the contact list.")
        main_menu()


def update_record():
    glance_list()
    name = input("What is the name of the person you'd like to update? > ")
    if name in contact_dict:
        old_value = input(f"Which of {name}'s attributes would you like to change? (type one) > favorite color | favorite fruit > ")
        print(f"{name}'s {old_value} is currently stored as {contact_dict[name][old_value]}.")
        new_value = input("What would you like to change it to? > ")
        contact_dict[name][old_value] = new_value
        print(f"{name}'s record has been updated:")
        print(contact_dict[name])
    if name not in contact_dict:
        print(f"There is no one by the name of {name} stored in the contact list.")
        main_menu()
    main_menu()


def delete_record():
    glance_list()
    name = input("Who would you like to delete? > ")
    if name in contact_dict:
        print(contact_dict[name])
        double_check = input(f"Are you sure you want to delete all data for {name}? > yes | no > ")
        if double_check == 'yes':
            contact_dict.pop(name)
            print(f"The entry for {name} has been deleted.")
        else:
            print("Returning to the main menu...")
            main_menu()
    elif name not in contact_dict:
        print(f"There is no one by the name of {name} stored in the contact list.")
        main_menu()
    main_menu()


main_menu()


