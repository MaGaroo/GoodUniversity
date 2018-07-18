from utils import get_input, get_secret_input, show_messages


class LoginView(object):
    def run(self, site, messages=None):
        site.clear()
        site.print_header()
        show_messages(messages)
        username = get_input('Username or Student Serial: ')
        password = get_secret_input('Password: ')
        user = site.get_user(username, password)
        if user is None:
            site.state = '/'
            return ["Bad username or password :("]
        if not user.verified:
            site.state = '/'
            return ["This user hasn't been verified yet :("]
        else:
            site.active_user = user
            site.state = '/{}/'.format(user.role.lower())
        return None
