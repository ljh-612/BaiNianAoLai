from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_me import PageMe
from page.page_register import PageRegister
from page.page_setting import PageSetting


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def home(self):
        return PageHome(self.driver)

    @property
    def register(self):
        return PageRegister(self.driver)

    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def me(self):
        return PageMe(self.driver)

    @property
    def setting(self):
        return PageSetting(self.driver)