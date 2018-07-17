from utils import choose_from_menu, show_messages


class IndexView(object):
    MENU = {
        "Login": "/login/",
        "Register": "/register/",
    }

    def run(self, site, messages=None):
        site.clear()
        site.print_header()
        show_messages(messages)
        choice = choose_from_menu(self.MENU.keys())
        site.state = self.MENU[choice]
        return 0
