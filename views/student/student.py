from utils import show_messages, choose_from_menu


class StudentView(object):
    MENU = {
        'Courses': '/student/courses/',
        'Workbook': '/student/workbook/',
        'Add Course': '/student/choose_course/',
        'Rate Teachers': '/student/assessment/',
        'Edit Profile': '/student/edit_profile/',
        'Change Password': '/change_password/',
        'Logout': '/logout/',
    }

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        choice = choose_from_menu(self.MENU.keys())
        site.state = self.MENU[choice]
        return None
