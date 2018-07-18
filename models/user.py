class User(object):
    ROLES = (
        "Student",
        "Teacher",
        "Manager",
    )

    def __init__(self, username=None, serial=None, name=None, password=None, email=None, field=None, phone_number=None,
                 role=None, verified=False):
        self.username = username
        self.serial = serial
        self.name = name
        self.password = password
        self.email = email
        self.field = field
        self.phone_number = phone_number
        self.role = role
        self.verified = verified

        self.errors = []
        self.courses = []
        self.course_list = []
        self.scores = {}
        self.site = None

    def is_valid(self, instance_list):
        if self.username is not None and type(self.username) != str:
            return False
        if self.serial is not None and type(self.serial) != str:
            return False
        if self.password is not None and type(self.password) != str:
            return False
        if self.email is not None and type(self.email) != str:
            return False
        if self.phone_number is not None and type(self.phone_number) != str:
            return False
        if self.name is not None and type(self.name) != str:
            return False
        if self.field is not None and type(self.field) != str:
            return False
        if type(self.verified) != bool:
            return False

        self.errors = []

        if not self.username and not self.serial:
            self.errors.append('At least one of the Username and Serial must not be empty.')
            return False

        for instance in instance_list:
            if self.username and instance.username == self.username:
                self.errors.append('This username already exists in the system.')
                return False
            if self.serial and instance.serial == self.serial:
                self.errors.append('This serial number already exists in the system.')
                return False

        if self.phone_number:
            for d in self.phone_number:
                if d not in '0123456789':
                    self.errors.append('The phone number must contain only digits.')
                    return False

        if self.serial:
            for d in self.serial:
                if d not in '0123456789':
                    self.errors.append('The serial number must contain only digits.')
                    return False

        if self.role not in self.ROLES:
            self.errors.append('This role does not exist in the system.')
            return False

        if self.role == 'Student' and self.serial is None:
            self.errors.append('Students must have serial number.')
            return False

        return True

    def get_average_score(self):
        if len(self.scores) == 0:
            return 20
        score_sum = 0
        for course in self.scores:
            score_sum += self.scores[course]
        return float(score_sum) / len(self.scores)

    def get_score_columns_title(self):
        return ['Course', 'Score']

    def get_scores(self):
        return [[course.title, self.scores[course]] for course in self.scores]

    def has_course(self, course):
        return course in self.course_list or course in self.scores

    def get_current_courses(self):
        return [course for course in self.course_list if course not in self.scores]

    def add_course(self, course):
        self.course_list.append(course)

    def as_list(self):
        return [self.username, self.serial, self.phone_number]

    def get_columns_title(self):
        return ['Username', 'Students No.', 'Phone']
