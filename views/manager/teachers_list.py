from utils import show_messages, paginator, choose_from_menu, pprint_table


# prints a table containing list of all teachers of the department
class TeachersListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        teacher_list = paginator(site.get_verified_teachers(), 20)
        page_number = 0
        while True:
            if len(teacher_list) == 0:
                print("There is no teacher in the system.")
            else:
                pprint_table('Students', teacher_list[page_number],
                             foot='Page {} of {}'.format(page_number + 1, len(teacher_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(teacher_list):
                menu.append('Next Page')
            if len(teacher_list) > 0:
                menu.append('Select')
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
        return None
