class Site(object):
    def __init__(self):
        self.active_user = None
        self.state = '/'
        self.user_list = []
        self.course_list = []

    @staticmethod
    def clear(self):
        print(chr(27) + "[2J")

    def print_header(self):
        pass

    def get_verified_students(self):
        pass

    def get_verified_teachers(self):
        pass

    def get_verified_courses(self):
        pass

    def get_unverified_users(self):
        pass

    def get_unverified_courses(self):
        pass

    def accept_course(self, course):
        pass

    def reject_course(self, course):
        pass

    def get_current_courses(self, user):
        pass

    def student_has_course(self, student, course):
        pass

    def add_user(self, user):
        pass

    def add_course(self, course):
        pass

    def add_course_for_user(self, user, course):
        pass
