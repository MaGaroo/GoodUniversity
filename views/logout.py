# after a user is done with the system he comes into this view and then will be logged out
class LogoutView(object):
    def run(self, site, messages=None):
        site.state = '/'
        return ['You successfully logged out from the system.']
