'''
v4 Now we'll ask the user for the distance, the starting units, and the units to convert to.

'''
selected_unit = input("Pick a unit of measurement: inches, feet, yards, miles, meters, or kilometers. > ")
selected_number = float(input("And now pick a number. > "))
print(f"You've selected {selected_number} {selected_unit}.")

# Converts to meters
if selected_unit == 'inches':
    conversion = selected_number * 0.0254

elif selected_unit == 'feet':
    conversion = selected_number * 0.3048

elif selected_unit == 'yards':
    conversion = selected_number * 0.9144

elif selected_unit == 'miles':
    conversion = selected_number * 1609.34

elif selected_unit == 'meters':
    conversion = selected_number

elif selected_unit == 'kilometers':
    conversion = selected_number * 1000

print(f"That equates to {conversion} meters.")

output = input("To which unit of measurement would you like to convert: inches, feet, yards, miles, meters, or kilometers? > ")


# Converts meters to selected unit

if output == 'inches':
    final_result = conversion / 0.0254

elif output == 'feet':
    final_result = conversion / 0.3048

elif output == 'yards':
    final_result = conversion / 0.9144

elif output == 'miles':
    final_result = conversion / 1609.34

elif output == 'meters':
    final_result = conversion

elif output == 'kilometers':
    final_result = conversion / 1000

print(f"{selected_number} {selected_unit} is equal to {final_result} {output}.")