from utils import show_messages, get_input


# lets the teachers to add a score for a student of a course
class AddScoreView(object):

    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        course = get_input('Course Serial: ')
        course = site.get_course(serial=course)
        if course is None:
            return ["No such course!"]
        elif course.owner != site.active_user:
            return ["You don't have permission to add score to this course."]
        elif not course.verified:
            return ["This course hasn't been verified yet."]
        student = get_input('Student Serial Number: ')
        student = site.get_student(serial=student)
        if student is None:
            return ["No such student!"]
        elif not student.has_course(course):
            return ["This student has not this course."]
        elif student.passed_course(course):
            return ["This student already has a score fot this course."]
        elif not student.verified:
            return ["This student hasn't been verified yet."]

        value = get_input('Score: ', output_type=int)

        student.scores[course] = value
        site.state = '/teacher/'
        return ['We added score successfully.']
