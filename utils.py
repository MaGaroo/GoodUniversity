# in this file we create some functions that may be commonly used in different parts of the project
import getpass


# return a string with the given length that has s in its middle and almost equal number of spaces around it
def center(s, length):
    diff = length - len(str(s))
    left_len = diff // 2
    right_len = diff - left_len
    return '{}{}{}'.format(' ' * left_len, s, ' ' * right_len)


# given the length of each cell of a table row, return the string that separates rows from each other
def row_separator(lens):
    result = '+'
    for length in lens:
        result += length * '-'
        result += '+'
    return result


# given the values of each cell of a specific row and length of each row, return the string of whole row
def get_row_string(row, lens):
    result = '|'
    for i, word in enumerate(row):
        result += center(word, lens[i])
        result += '|'
    return result


# print a table in a pretty manner
def pprint_table(head, rows, foot=None, cols_title=None):
    # cast rows objects to list
    if type(rows[0]) != list:
        if cols_title is None:
            cols_title = rows[0].get_columns_title()
        for i in range(len(rows)):
            rows[i] = rows[i].as_list()

    # add row number column to the table
    if cols_title[0] != '#':
        cols_title = ['#'] + cols_title
        for i in range(len(rows)):
            rows[i] = [i + 1] + rows[i]

    # add title to the top of rows objects
    rows = [cols_title] + rows

    # calculate length of each cell in different columns and
    # length of the header and footer parts of the table
    max_len = [0] * len(rows[0])
    for row in rows:
        for i, word in enumerate(row):
            max_len[i] = max(max_len[i], len(str(word)) + 2)

    while sum(max_len) + len(max_len) - 1 < len(head) + 2:
        max_len[-1] += 1

    if foot:
        while sum(max_len) + len(max_len) - 1 < len(foot) + 2:
            max_len[-1] += 1

    head_len = sum(max_len) + len(max_len) - 1

    # find the string that separates rows from each other
    current_row_separator = row_separator(max_len)

    # print table
    print('+{}+'.format('-' * head_len))
    print('|{}|'.format(center(head, head_len)))
    print(current_row_separator)
    for row in rows:
        print(get_row_string(row, max_len))
        print(current_row_separator)

    if foot:
        print('|{}|'.format(center(foot, head_len)))
    print('+{}+'.format('-' * head_len))

    return


# given a menu, force user to choose one of its items
def choose_from_menu(menu, message=None):
    if message is None:
        message = 'Please enter your choice number: '
    menu = list(menu)

    for id, item in enumerate(menu):
        print(id, item)
    print()
    while True:
        choice = input(message)
        try:
            choice = int(choice)
        except Exception as _:
            print("Invalid choice!")
            continue
        if choice < 0 or choice >= len(menu):
            print("Invalid choice!")
        else:
            return menu[choice]


# read something from input, with request message equal to 'message' and output_type type!
# if null equals True, the input may be blank and None will be returned
def get_input(message, output_type=str, null=False):
    while True:
        result = input(message)
        if len(result) == 0:
            if null:
                return None
            else:
                print("Blank input is not allowed!")
                continue
        try:
            return output_type(result)
        except Exception as _:
            print("Invalid input!")


# it acts exactly like get_input function, but user can't see what characters he has entered
# it can be used to read password
def get_secret_input(message, output_type=str, null=False):
    while True:
        result = getpass.getpass(prompt=message)
        if len(result) == 0:
            if null:
                return None
            else:
                print("Blank input is not allowed!")
                continue
        try:
            return output_type(result)
        except Exception as _:
            print("Invalid input!")


# prints system messages and notifications
def show_messages(message_list):
    if message_list is None:
        return
    print()
    for message in message_list:
        print('** ' + message)
    print()


# slices the array into consecutive parts with length equal to per_page (note: except the last piece)
def paginator(array, per_page):
    result = []
    left = 0
    while left < len(array):
        result.append(array[left:min(len(array), left + per_page)])
        left += per_page
    return result
