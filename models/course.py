from models.user import User


class Course(object):
    def __init__(self, serial, title, owner, verified=False):
        self.serial = serial
        self.title = title
        self.verified = verified
        self.owner = owner
        self.errors = None

    def is_valid(self, instance_list):
        self.errors = []
        if self.serial is None:
            self.errors.append('Serial must not be empty.')
            return False
        if self.title is None:
            self.errors.append('Title must not be empty.')
            return False
        if self.owner is None or type(self.owner) != User or self.owner.role != "Teacher":
            self.errors.append('The course must have an owner with teacher role.')
            return False
        return True

    def get_columns_title(self):
        return ['Title', 'Teacher', 'Serial No.', 'Verified']

    def as_list(self):
        return [self.title, self.owner.name, self.serial, 'Yes' if self.verified else 'No']
