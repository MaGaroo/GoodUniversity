import copy

from utils import show_messages, paginator, choose_from_menu, get_input, pprint_table


class NewUsersListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        user_list = paginator(site.get_unverified_users(), 20)
        page_number = 0
        while True:
            if len(user_list) == 0:
                print("There is no unverified user in the system.\n")
            else:
                pprint_table('New Users', copy.copy(user_list[page_number]),
                             foot='Page {} of {}'.format(page_number + 1, len(user_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(user_list):
                menu.append('Next Page')
            if len(user_list) > 0:
                menu.append('Accept')
                menu.append('Reject')
            choice = choose_from_menu(menu)
            if choice == 'Home':
                site.state = '/manager/'
                break
            elif choice == 'Previous Page':
                page_number -= 1
                site.clear()
            elif choice == 'Next Page':
                page_number += 1
                site.clear()
            else:
                student_row = get_input("Enter row number of the student: ", output_type=int)
                student_row -= 1
                if student_row >= len(user_list[page_number]) or student_row < 0:
                    return ['Invalid row number!']
                if choice == 'Accept':
                    site.accept_user(user_list[page_number][student_row])
                else:
                    site.reject_user(user_list[page_number][student_row])
                return ['Operation completed successfully.']
        return None
