class User(object):
    count = 0

    ROLES = (
        "Student",
        "Teacher",
        "Manager",
    )

    def __init__(self, username=None, serial=None, password=None, email=None, phone_number=None, role=None,
                 verified=False):
        self.pk = User.count
        User.count += 1
        self.username = username
        self.serial = serial
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.role = role
        self.verified = verified
        self.errors = []

    def is_valid(self, instance_list):
        if type(self.username) != str:
            return False
        if type(self.serial) != str:
            return False
        if type(self.password) != str:
            return False
        if type(self.email) != str:
            return False
        if type(self.phone_number) != str:
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
            if self.serial and instance.number == self.serial:
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
        pass

    def get_scores(self):
        pass
