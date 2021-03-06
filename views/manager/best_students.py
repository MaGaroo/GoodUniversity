from utils import show_messages, paginator, choose_from_menu, pprint_table


# runs when the manager wants to see the students with highest average scores
class BestStudentsView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        student_list = [(student.get_average_score(), student) for student in site.get_verified_students()]
        student_list.sort()
        student_list = student_list[::-1]
        student_list = [[t[0], t[1].name, t[1].serial, t[1].field] for t in student_list]
        student_list = paginator(student_list, 20)
        page_number = 0
        while True:
            if len(student_list) == 0:
                print("There is no verified students in the system.\n")
            else:
                pprint_table('Students', student_list[page_number],
                             foot='Page {} of {}'.format(page_number + 1, len(student_list)),
                             cols_title=['Avg. Score', 'Name', 'Student No.', 'Field'])
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(student_list):
                menu.append('Next Page')
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
