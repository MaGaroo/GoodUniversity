from models.user import User
from utils import get_input, get_secret_input, show_messages, choose_from_menu


class RegisterView(object):
    def run(self, site, messages=None):
        site.clear()
        site.print_header()
        show_messages(messages)
        username = get_input('Username(left blank if you want): ', null=True)
        # TODO: change blank into null
        serial = get_input('Serial Number(left blank if you want): ', null=True)
        email = get_input('Email Address: ')
        role = choose_from_menu(User.ROLES, message="What's your role? ")
        phone_number = get_input('Phone Number: ')
        password = get_secret_input('Password: ')
        password2 = get_secret_input('Password Again: ')

        if password != password2:
            return ["Passwords do not match."]

        user = User(username=username,
                    serial=serial,
                    email=email,
                    role=role,
                    phone_number=phone_number,
                    password=password)
        if user.is_valid(site.user_list):
            site.add_user(user)
            site.state = '/'
            return ['You successfully registered in the system. Wait for the manager to verify you.']
        else:
            return user.errors
