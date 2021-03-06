from models.user import User
from utils import get_input, get_secret_input, show_messages, choose_from_menu


# when somebody wants to use the system and has not an account, he can create one in this view and
# wait for the system manager to verify his account
class RegisterView(object):
    def run(self, site, messages=None):
        site.clear()
        site.print_header()
        show_messages(messages)
        username = get_input('Username(left blank if you want): ', null=True)
        serial = get_input('Serial Number(left blank if you want): ', null=True)
        name = get_input('Name: ')
        field = get_input('Field: ')
        email = get_input('Email Address: ')
        role = choose_from_menu(User.ROLES, message="What's your role? ")
        phone_number = get_input('Phone Number: ')
        password = get_secret_input('Password: ')
        password2 = get_secret_input('Password Again: ')

        if password != password2:
            return ["Passwords do not match."]

        user = User(
            username=username,
            serial=serial,
            email=email,
            role=role,
            phone_number=phone_number,
            password=password,
            name=name,
            field=field
        )
        if user.is_valid(site.user_list):
            site.add_user(user)
            site.state = '/'
            return ['You successfully registered in the system. Wait for the manager to verify you.']
        else:
            return user.errors
