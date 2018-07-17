class Course(object):
    count = 0

    def __init__(self, serial, title, owner, verified=False):
        self.pk = Course.count
        Course.count += 1
        self.serial = serial
        self.title = title
        self.verified = verified
        self.owner = owner.pk
        self.errors = None

    def is_valid(self, instance_list):
        pass
