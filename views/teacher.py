from utils import show_messages, choose_from_menu


class StudentView(object):
    MENU = {
        'Courses': '/teacher/courses/',
        'Students': '/teacher/students/',
        'Course Request': '/teacher/course_request/',
        'Add Scores': '/teacher/scores/',
        'Edit Profile': '/teacher/edit_profile/',
        'Change Password': '/change_password/',
        'Logout': '/logout/',
    }

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        choice = choose_from_menu(self.MENU.keys())
        site.state = self.MENU[choice]
        return None
