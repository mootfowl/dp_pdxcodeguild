'''

LAB22: Practice Problems 2

'''

numbers_list = []

while True:
    prompt = input("Enter a number or 'done' > ")
    if prompt == "done":
        print(numbers_list)
        exit()

    else:
        numbers_list.append(int(prompt))

