import getpass


def center(s, length):
    diff = length - len(str(s))
    left_len = diff // 2
    right_len = diff - left_len
    return '{}{}{}'.format(' ' * left_len, s, ' ' * right_len)


def row_separator(lens):
    result = '+'
    for length in lens:
        result += length * '-'
        result += '+'
    return result


def get_row_string(row, lens):
    result = '|'
    for i, word in enumerate(row):
        result += center(word, lens[i])
        result += '|'
    return result


def pprint_table(head, rows, foot=None, cols_title=None):
    if type(rows[0]) != list:
        if cols_title is None:
            cols_title = rows[0].get_columns_title()
        for i in range(len(rows)):
            rows[i] = rows[i].as_list()

    if cols_title[0] != '#':
        cols_title = ['#'] + cols_title
        for i in range(len(rows)):
            rows[i] = [i + 1] + rows[i]

    rows = [cols_title] + rows

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
    current_row_separator = row_separator(max_len)

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


def show_messages(message_list):
    if message_list is None:
        return
    print()
    for message in message_list:
        print('** ' + message)
    print()


def paginator(array, per_page):
    result = []
    left = 0
    while left < len(array):
        result.append(array[left:min(len(array), left + per_page)])
        left += per_page
    return result
