from utils import show_messages, get_secret_input


# users change their password in this view
class ChangePasswordView(object):
    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)
        previous_password = get_secret_input('Previous Password: ')
        if previous_password != site.active_user.password:
            return ['You entered your previous password incorrectly.']
        new_password = get_secret_input('New Password: ')
        verify_password = get_secret_input('Verify it: ')
        if new_password != verify_password:
            return ['The passwords you entered do not match.']
        site.active_user.password = new_password
        site.state = '/{}/'.format(site.active_user.role.lower())
        return None
