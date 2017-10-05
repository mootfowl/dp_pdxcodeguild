'''
v1 unit converter: Ask the user for the number of feet, and print out the equivalent distance in meters.
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
'''

number_in_feet = float(input("Pick any number in feet, and we'll convert it to meters. > "))
number_in_meters = number_in_feet * 0.3048
print(f"{number_in_feet} feet is equivalent to {number_in_meters} meters.")

'''
v2 Allow the user to also enter the units. 
Then depending on the units, convert the distance into meters. 
The units we'll allow are feet, miles, meters, and kilometers.
'''

selected_unit = input("Pick a unit of measurement: feet, miles, meters, or kilometers. > ")
selected_number = float(input("And now pick a number. > "))

if selected_unit == 'feet':
    conversion = selected_number * 0.3048
    print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")

elif selected_unit == 'miles':
    conversion = selected_number * 1609.34
    print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")

elif selected_unit == 'meters':
    print(f"{selected_number} {selected_unit} is equal to {conversion} meters. DUH.")

elif selected_unit == 'kilometers':
    conversion = selected_number / 1000
    print(f"{selected_number} {selected_unit} is equal to {conversion} meters.")

