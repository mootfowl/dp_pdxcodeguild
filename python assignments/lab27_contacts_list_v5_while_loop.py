'''

LAB27: Contact List v5

Edited to use a while loop instead of a main_menu function.

'''

# from twilio.rest import Client


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


def view_all_records():
    for person in contact_dict:
        print(contact_dict[person])


def create_record():
    name = input("What is the new contact's first name? > ")
    color = input("What is their favorite color? > ")
    fruit = input("And most importantly, what is their favorite fruit? > ")
    phone = input("And finally, what is their phone number? > ")
    contact_dict.update({name: {'name': name, 'favorite color': color, 'favorite fruit': fruit, 'phone number': phone}})
    print(f"A new entry for {name} has been created:")
    print(contact_dict[name])


def glance_list(): # This improves the UX for the update, delete, and retrieve functions
    all = []
    for person in contact_dict:
        all.append(person)
        all.sort() # Alphabetizes the list of people
    print(f"CONTACTS: {all}")


def retrieve_record():
    glance_list()
    name = input("Who are you looking for? > ")
    if name in contact_dict:
        print(contact_dict[name])
        main_menu()
    elif name not in contact_dict:
        print(f"There is no one by the name of {name} stored in the contact list.")


def update_record():
    glance_list()
    name = input("What is the name of the person you'd like to update? > ")
    if name in contact_dict:
        old_value = input(f"Which of {name}'s attributes would you like to change? (type one) > favorite color | favorite fruit | phone number > ")
        print(f"{name}'s {old_value} is currently stored as {contact_dict[name][old_value]}.")
        new_value = input("What would you like to change it to? > ")
        contact_dict[name][old_value] = new_value
        print(f"{name}'s record has been updated:")
        print(contact_dict[name])
    if name not in contact_dict:
        print(f"There is no one by the name of {name} stored in the contact list.")


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


def send_message():
    glance_list()
    recipient = input("Who would you like to message? > ")
    if recipient in contact_dict:
        sms = input("What would you like to send to them? > ")
        account_sid = "xxxx"
        auth_token = "xxxx"
        client = Client(account_sid, auth_token)
        message = client.api.account.messages.create(to=contact_dict[recipient]['phone number'],
                                                     from_="+19718033720",
                                                     body=sms)
    if recipient not in contact_dict:
        print(f"There is no one by the name of {recipient} stored in the contact list.")


def save_and_exit():
    save_check = input("Would you like to save your changes before exiting? > yes | no > ")
    if save_check == 'yes':
        print("Saving...")
        save_list = []
        for name in contact_dict:
            save_list.append(','.join(list(contact_dict[name].values())))
        save_list.insert(0, ','.join(key))
        print("Changes saved. Goodbye.")
        with open('lab27_contacts_save.csv', 'w') as file:
            file.write('\n'.join(save_list))
        exit()
    if save_check == 'no':
        print("Goodbye.")
        exit()

while True:
    selection = input("\nCONTACT LIST - Main Menu"
                      "\n(type one) > view all | create | retrieve | update | delete | message | exit > ")
    if selection == 'view all':
        view_all_records()
    elif selection == 'create':
        create_record()
    elif selection == 'retrieve':
        retrieve_record()
    elif selection == 'update':
        update_record()
    elif selection == 'delete':
        delete_record()
    elif selection == 'message':
        send_message()
    elif selection == 'exit':
        save_and_exit()
