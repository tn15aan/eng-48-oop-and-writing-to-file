from users_class import *

def open_txt_file(file_name):
    try:
        list_of_users = []
        opened_file = open(file_name, 'r')
        lines = opened_file.readlines()
        for line in lines:
            name = line.split(' ')
            list_of_users.append(name)
            print(list_of_users)
        opened_file.close()  # closes the file so it can be used by other programs
    except FileNotFoundError as errMsg:  # the ass errorMsg captures the original message
        print('Check file name &/or path - File cannot be found')
        print(errMsg)  # printing original message
    finally:
        print('////Program closing - execution completed')

open_txt_file('names.txt')

# print('Output text file')
output_text_file('names.txt')
