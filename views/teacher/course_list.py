from utils import show_messages, choose_from_menu, paginator, pprint_table


class TeacherCourseListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course_list = paginator(site.active_user.get_current_courses(), 20)
        page_number = 0
        while True:
            menu = {
                'Home': '/teacher/',
            }
            if page_number - 1 >= 0:
                menu['Previous Page'] = '/teacher/courses/'
            if page_number + 1 < len(course_list):
                menu['Next Page'] = '/teacher/courses/'
            pprint_table('Courses', course_list[page_number],
                         foot='Page {} of {}'.format(page_number, len(course_list)))
            choice = choose_from_menu(menu.keys())
            if choice == 'Home':
                site.state = menu[choice]
                break
            elif choice == 'Previous Page':
                page_number -= 1
            elif choice == 'Next Page':
                page_number += 1

        return None
