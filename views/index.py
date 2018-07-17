from utils import choose_from_menu


class IndexView(object):
    MENU = {
        "Login": "/login/",
        "Register": "/register/",
    }

    def run(self, site):
        site.print_header()
        choice = choose_from_menu(site, self.MENU.keys())
        site.state = self.MENU[choice]
        return 0
