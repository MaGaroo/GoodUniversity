from utils import show_messages, paginator, choose_from_menu, get_input, pprint_table


class CourseRequestsListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course_list = paginator(site.get_unverified_users(site.active_courses), 20)
        page_number = 0
        while True:
            pprint_table('Course Requests', course_list[page_number],
                         foot='Page {} of {}'.format(page_number, len(course_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(course_list):
                menu.append('Next Page')
            menu.append('Accept')
            menu.append('Reject')
            choice = choose_from_menu(menu)
            if choice == 'Home':
                site.state = '/manager/'
                break
            elif choice == 'Previous Page':
                page_number -= 1
            elif choice == 'Next Page':
                page_number += 1
            else:
                course_row = get_input("Enter row number of the course: ")
                if course_row >= len(course_list[page_number]) or course_row < 0:
                    return ['Invalid row number!']
                if choice == 'Accept':
                    site.accept_course(course_list[page_number][course_row])
                else:
                    site.reject_course(course_list[page_number][course_row])
                return ['Operation completed successfully.']
        return None