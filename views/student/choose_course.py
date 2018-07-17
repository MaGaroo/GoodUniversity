from utils import show_messages, paginator, choose_from_menu, get_input, pprint_table


class ChooseCourseView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course_list = paginator(site.get_available_courses(site.active_user), 20)
        page_number = 0
        while True:
            pprint_table('Available Courses', site.get_available_courses(site.active_user),
                         foot='Page {} of {}'.format(page_number, len(course_list)))
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(course_list):
                menu.append('Next Page')
            menu.append('Select')
            choice = choose_from_menu(menu)
            if choice == 'Home':
                site.state = '/'
                break
            elif choice == 'Previous Page':
                page_number -= 1
            elif choice == 'Next Page':
                page_number += 1
            else:
                course_row = get_input("Enter row number of the course to get it: ")
                if course_row >= len(course_list[page_number]) or course_row < 0:
                    return ['Invalid row number!']
                site.add_course_for_user(site.active_user, course_list[page_number][course_row])
                return ['You added course successfully.']
        return None
