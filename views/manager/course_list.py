from utils import show_messages, choose_from_menu, paginator, pprint_table


# runs when manager wants to see the list of courses in the department
class ManagerCourseListView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course_list = paginator(site.get_verified_courses(), 20)
        page_number = 0
        while True:
            menu = ['Home']
            if page_number - 1 >= 0:
                menu.append('Previous Page')
            if page_number + 1 < len(course_list):
                menu.append('Next Page')
            if len(course_list) == 0:
                print("There is no verified course in the system.")
            else:
                pprint_table('Courses', course_list[page_number],
                             foot='Page {} of {}'.format(page_number + 1, len(course_list)))
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
