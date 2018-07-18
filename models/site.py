import jdatetime

from models.course import Course
from models.user import User
from states import state_list
from utils import center


class Site(object):
    # loads some users and course to test
    def load_test(self):
        admin = User(
            username='admin',
            password='admin',
            role='Manager',
            email='admin@localhost',
            phone_number='09123456789',
            serial='96000000',
            verified=True
        )
        self.user_list.append(admin)

        teacher = User(
            username='2',
            password='2',
            name='Moallem',
            role='Teacher',
            email='2@localhost',
            phone_number='09123456789',
            serial=None,
            verified=True
        )
        self.user_list.append(teacher)

        student = User(
            username='1',
            password='1',
            role='Student',
            email='1@localhost',
            phone_number='09123456789',
            serial='96000001',
            field='Math',
            verified=True,
            name='Mammad Sarab'
        )
        self.user_list.append(student)

        course = Course(
            serial='40122',
            owner=teacher,
            title='Stats',
            verified=True
        )
        self.course_list.append(course)
        teacher.course_list.append(course)

    def __init__(self):
        self.active_user = None
        self.state = '/'
        self.user_list = []
        self.course_list = []

        self.load_test()

    # program main loop
    def run(self):
        messages = None
        while True:
            view = state_list[self.state]()
            messages = view.run(self, messages)

    # clears screen
    def clear(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    # prints header of site (contains project name and datetime)
    def print_header(self):
        print('+' + 50 * '-' + '+')
        print('|' + 50 * ' ' + '|')
        print('|' + 21 * ' ' + 'natseloG' + ' ' * 21 + '|')
        print('|{}|'.format(center(jdatetime.datetime.now().strftime("%d %b %Y || %H:%M"), 50)))
        print('|' + 50 * ' ' + '|')
        print('+' + 50 * '-' + '+')

    # returns a list of verified students
    def get_verified_students(self):
        result = []
        for user in self.user_list:
            if user.role == 'Student' and user.verified:
                result.append(user)
        return result

    # returns a list of verified teachers
    def get_verified_teachers(self):
        result = []
        for user in self.user_list:
            if user.role == 'Teacher' and user.verified:
                result.append(user)
        return result

    # returns a list of verified courses
    def get_verified_courses(self):
        result = []
        for course in self.course_list:
            if course.verified:
                result.append(course)
        return result

    # returns a list of non-verified users
    def get_unverified_users(self):
        result = []
        for user in self.user_list:
            if not user.verified:
                result.append(user)
        return result

    # returns a list of non-verified courses
    def get_unverified_courses(self):
        result = []
        for course in self.course_list:
            if not course.verified:
                result.append(course)
        return result

    # verifies a course
    def accept_course(self, course):
        course.verified = True

    # rejects a course
    def reject_course(self, course):
        course.owner.course_list.remove(course)
        self.course_list.remove(course)

    # verifies user
    def accept_user(self, user):
        user.verified = True

    # rejects user
    def reject_user(self, user):
        for instance in self.course_list:
            if instance == user:
                self.course_list.remove(instance)

    # returns a list of courses. if user is teacher, returns the courses which he owns.
    def get_current_courses(self, user):
        if user.role == 'Student':
            return [course for course in user.course_list if course not in user.scores]
        else:
            return [course for course in user.course_list if course not in user.scores]

    # adds a user
    def add_user(self, user):
        user.site = self
        self.user_list.append(user)

    # adds course
    def add_course(self, course):
        course.site = self
        self.course_list.append(course)
        course.owner.course_list.append(course)

    # gets a user with specified fields
    def get_user(self, username, password):
        for user in self.user_list:
            if user.username.lower() == username.lower() and user.password == password:
                return user
        return None

    # returns available courses
    def get_available_courses(self):
        result = []
        for course in self.course_list:
            if not self.active_user.has_course(course) and course.verified:
                result.append(course)
        return result

    # returns a course by its serial
    def get_course(self, serial):
        for course in self.course_list:
            if course.serial == serial:
                return course
        return None

    def get_student(self, serial):
        for user in self.user_list:
            if user.role == 'Student' and user.serial == serial:
                return user
        return None
