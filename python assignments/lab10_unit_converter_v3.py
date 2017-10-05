'''
v3 Allow the user to also enter the units.
Then depending on the units, convert the distance into meters.
The units we'll allow are inches, feet, yards, miles, meters, and kilometers.
'''

def number_crunch():
    selected_unit = input("Pick a unit of measurement: inches, feet, yards, miles, meters, or kilometers. > ")
    selected_number = float(input("And now pick a number. > "))

    if selected_unit == 'inches':
        conversion = selected_number * 0.0254
        print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")
        number_crunch()

    elif selected_unit == 'feet':
        conversion = selected_number * 0.3048
        print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")
        number_crunch()

    elif selected_unit == 'yards':
        conversion = selected_number * 0.9144
        number_crunch()

    elif selected_unit == 'miles':
        conversion = selected_number * 1609.34
        print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")
        number_crunch()

    elif selected_unit == 'meters':
        conversion = selected_number
        print(f"{selected_number} {selected_unit} is equal to {conversion} meters. DUH.")
        number_crunch()

    elif selected_unit == 'kilometers':
        conversion = selected_number / 1000
        print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")
        number_crunch()

number_crunch()
