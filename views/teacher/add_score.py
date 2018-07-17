from utils import show_messages, get_input


class AddScoreView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course = get_input('Course Serial: ')
        course = site.get_course(serial=course)
        if course is None:
            return ["No such course!"]
        elif course.owner != site.active_user.pk:
            return ["You don't have permission to add score to this course!"]
        elif not course.verified:
            return ["This course hasn't been verified yet!"]
        student = get_input('Student Serial Number: ')
        student = site.get_student(serial=student)
        if student is None:
            return ["No such student!"]
        elif not site.student_has_course(student, course):
            return ["This student has not this course."]
        elif not student.verified:
            return ["This student is not verified yet."]

        value = get_input('Score: ', output_type=int)

        student.score[course.pk] = value

        return None
