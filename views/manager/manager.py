from utils import show_messages, choose_from_menu


class TeacherView(object):
    MENU = {
        'Teachers': '/manager/teachers/',
        'Students': '/manager/students/',
        'Courses': '/manager/courses/',
        'Course Requests': '/manager/course_requests/',
        'Unverified Students': '/manager/new_users/',
        'Best Students': '/manager/best_students/',
        'Edit Profile': '/manager/edit_profile/',
        'Change Password': '/change_password/',
        'Logout': '/logout/',
    }

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        choice = choose_from_menu(self.MENU.keys())
        site.state = self.MENU[choice]
        return None
