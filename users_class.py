class Users():
    def __init__(self, name):
        self.name = name


def output_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip('\n'))
    except FileNotFoundError as error:
        print('Check your file')
        print(error)
    finally:
        print('////Program closing - execution completed')

