from utils import show_messages, choose_from_menu, paginator, pprint_table


class WorkbookView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course_list = paginator(site.active_user.get_scores(), 20)
        page_number = 0
        while True:
            menu = {
                'Home': '/student/',
            }
            if page_number - 1 >= 0:
                menu['Previous Page'] = '/student/workbook/'
            if page_number + 1 < len(course_list):
                menu['Next Page'] = '/student/workbook/'
            if len(course_list) == 0:
                print("There is no passed course in the system.")
            else:
                pprint_table('Workbook', course_list[page_number],
                             foot='Page {} of {}'.format(page_number + 1, len(course_list)),
                             cols_title=site.active_user.get_score_columns_title())
            choice = choose_from_menu(menu.keys())
            if choice == 'Home':
                site.state = menu[choice]
                break
            elif choice == 'Previous Page':
                page_number -= 1
                site.clear()
            elif choice == 'Next Page':
                page_number += 1
                site.clear()

        return None
