class Course(object):
    def __init__(self, serial, title, owner, verified=False):
        self.serial = serial
        self.title = title
        self.verified = False
        self.owner = owner.pk
        self.errors = None

    def is_valid(self, instance_list):
        pass
