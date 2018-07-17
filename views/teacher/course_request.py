from models.course import Course
from utils import show_messages, get_input


class CourseRequestView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        serial = get_input('Course Serial: ')
        title = get_input('Title: ')

        course = Course(serial=serial, title=title, owner=site.active_user)
        if course.is_valid(site.course_list):
            site.add_course(course)
        else:
            return course.errors

        return None
