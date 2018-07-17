class LogoutView(object):
    def run(self, site, messages=None):
        site.state = '/'
        return ['You successfully logged out from the system.']
