from views.change_password import ChangePasswordView
from views.edit_profile import EditProfileView
from views.index import IndexView
from views.login import LoginView
from views.logout import LogoutView
from views.manager import ManagerView, TeachersListView, ManagerCourseListView, CourseRequestsListView, \
    NewUsersListView, BestStudentsView
from views.manager import StudentsListView as ManagerStudentsListView
from views.register import RegisterView
from views.student import StudentView, StudentCourseListView, WorkbookView, ChooseCourseView, AssessmentView
from views.teacher import TeacherView, TeacherCourseListView, StudentsListView, CourseRequestView, AddScoreView

# its a dictionary from all situation that users may have in the system to
# the view classes that must handle each of them
state_list = {

    "/": IndexView,
    "/login/": LoginView,
    "/register/": RegisterView,
    "/change_password/": ChangePasswordView,
    "/logout/": LogoutView,

    "/student/": StudentView,
    "/student/courses/": StudentCourseListView,
    "/student/workbook/": WorkbookView,
    "/student/choose_course/": ChooseCourseView,
    "/student/assessment/": AssessmentView,
    "/student/edit_profile/": EditProfileView,

    "/teacher/": TeacherView,
    "/teacher/courses/": TeacherCourseListView,
    "/teacher/students/": StudentsListView,
    "/teacher/course_request/": CourseRequestView,
    "/teacher/scores/": AddScoreView,
    "/teacher/edit_profile/": EditProfileView,

    "/manager/": ManagerView,
    "/manager/teachers/": TeachersListView,
    "/manager/students/": ManagerStudentsListView,
    "/manager/courses/": ManagerCourseListView,
    "/manager/course_requests/": CourseRequestsListView,
    "/manager/new_users/": NewUsersListView,
    "/manager/best_students/": BestStudentsView,
    "/manager/edit_profile/": EditProfileView,

}
