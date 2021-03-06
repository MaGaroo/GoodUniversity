import copy

from utils import show_messages, paginator, choose_from_menu, get_input, pprint_table


# runs when manager wants to accept or reject teachers' course requests
class CourseRequestsListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course_list = paginator(site.get_unverified_courses(), 20)
        page_number = 0
        while True:
            if len(course_list) == 0:
                print("There is no course request in the system.\n")
            else:
                pprint_table('Course Requests', copy.copy(course_list[page_number]),
                             foot='Page {} of {}'.format(page_number + 1, len(course_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(course_list):
                menu.append('Next Page')
            if len(course_list) > 0:
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
                course_row = get_input("Enter row number of the course: ", output_type=int)
                course_row -= 1
                if course_row >= len(course_list[page_number]) or course_row < 0:
                    return ['Invalid row number!']
                if choice == 'Accept':
                    site.accept_course(course_list[page_number][course_row])
                else:
                    site.reject_course(course_list[page_number][course_row])
                return ['Operation completed successfully.']
        return None
