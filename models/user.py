class User(object):
    ROLES = (
        "Student",
        "Teacher",
        "Manager",
    )

    def __init__(self, username=None, serial=None, password=None, email=None, phone_number=None, role=None):
        self.username = username
        self.serial = serial
        self.password = password
        self.email = email
        self.phone_number = phone_number
        self.role = role

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

        if not self.username and not self.serial:
            return False

        for instance in instance_list:
            if self.username and instance.username == self.username:
                return False
            if self.serial and instance.number == self.serial:
                return False

        if self.phone_number:
            for d in self.phone_number:
                if d not in '0123456789':
                    return False

        if self.serial:
            for d in self.serial:
                if d not in '0123456789':
                    return False

        if self.role not in self.ROLES:
            return False

        return True
