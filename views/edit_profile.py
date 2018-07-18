from utils import get_input, show_messages


class EditProfileView(object):
    def run(self, site, messages=None):
        site.clear()
        show_messages(messages)

        print("If you don't want to change a field, left it blank and just press ENTER.\n")

        name = get_input('Name: ', null=True)
        if name is not None:
            site.active_user.name = name

        email = get_input('Email Address: ', null=True)
        if email is None:
            site.active_user.email = email

        phone_number = get_input('Phone Number: ', null=True)
        if phone_number is None:
            site.active_user.phone_number = phone_number

        site.state = '/{}/'.format(site.active_user.role.lower())
        return None
