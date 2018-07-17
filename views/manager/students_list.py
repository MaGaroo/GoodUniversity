from utils import show_messages, paginator, choose_from_menu, pprint_table


class StudentsListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        student_list = paginator(site.get_verified_students(), 20)
        page_number = 0
        while True:
            pprint_table('Students', student_list[page_number],
                         foot='Page {} of {}'.format(page_number + 1, len(student_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(student_list):
                menu.append('Next Page')
            menu.append('Select')
            choice = choose_from_menu(menu)
            if choice == 'Home':
                site.state = '/manager/'
                break
            elif choice == 'Previous Page':
                page_number -= 1
            elif choice == 'Next Page':
                page_number += 1
        return None
