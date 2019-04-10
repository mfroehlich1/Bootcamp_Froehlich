# Define a function to read in the lines from the phonebook .readlines()?
# You'll also need to use the built-in open and with to load the file
# Store each line of the file in either a list of dictionaries or list of lists.

# Then display the information in the following format:
# Name: Mike - Location: Work - Number: 9738841123


def show_phonebook():
    with open('phonebook.txt') as fh:
        lines = ''
        for line in fh:
            col_list = ['Name', '- Location', '- Number']
            row_list = line.split()
            row_dict = dict(zip(col_list, row_list))

            lines += f'{str(row_dict)}\n'

            remove_list= ['{', '}', '\'', ',']
            for item in remove_list:
                lines = lines.replace(item, '')

        print(lines)

    return 1


def add_phonebook(name, location, number):
    fh = open("phonebook.txt", "a")
    line = f'{name} {location} {number}'
    fh.write(line)
    fh.close()

    return 1


while True:
    add_number = ''
    add_location= ''
    add_name = ''
    print('Would you like to:\n1. (show)\n2. (add)\n3. (quit)')
    choice = input("Choice: ")

    if choice == 'show':
        show_phonebook()
    elif choice == 'add':
        add_name = input('Name: ')
        add_location = input('Location: ')
        add_number = input('Number: ')
        add_phonebook(add_name, add_location, add_number)
        show_phonebook()
    elif choice == 'quit':
        break
    else:
        print("Choose a valid option!")
