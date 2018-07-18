import copy

from utils import show_messages, paginator, choose_from_menu, pprint_table, get_input


# shows the students a list containing all of the teachers and lets the students to rate teachers
class AssessmentView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        teacher_list = paginator(site.get_verified_teachers(), 20)
        page_number = 0
        while True:
            if len(teacher_list) == 0:
                print("There is no student in the system.")
            else:
                pprint_table('Teachers', copy.copy(teacher_list[page_number]),
                             foot='Page {} of {}'.format(page_number + 1, len(teacher_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(teacher_list):
                menu.append('Next Page')
            if len(teacher_list) > 0:
                menu.append('Rate')
            choice = choose_from_menu(menu)
            if choice == 'Home':
                site.state = '/student/'
                break
            elif choice == 'Previous Page':
                page_number -= 1
                site.clear()
            elif choice == 'Next Page':
                page_number += 1
                site.clear()
            else:
                teacher_row = get_input('Enter the row number of the teacher you wanna rate: ', output_type=int)
                teacher_row -= 1
                if teacher_row < 0 or teacher_row >= len(teacher_list[page_number]):
                    return ['Invalid row number!']
                rate = get_input('How do you rate this teacher?\nChoose a natural number from 1 to 5: ',
                                 output_type=int)
                if rate < 1 or rate > 5:
                    return ['Invalid rating!']
                teacher_list[page_number][teacher_row].rates[rate - 1] += 1
                return ['You rated the teacher successfully.']
        return None
