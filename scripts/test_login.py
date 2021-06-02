from time import sleep

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        # 确认应用是否需要刷新，TRUE=不刷新，FALSE=刷新
        self.driver = init_driver(False)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        self.page.home.page_home_click_me()
        self.page.register.page_go_login()
        self.page.login.page_login_input_username(username)
        self.page.login.page_login_input_password(password)
        self.page.login.page_login()
        if toast is None:
            assert self.page.me.get_nick_name_text_view() == username, "登录用户名不一致"
        else:
            self.page.login.page_login_find_toast(toast)
            self.page.login.page_login_get_toast(toast)