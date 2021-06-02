from time import sleep

import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        # 确认应用是否需要刷新，TRUE=不刷新，FALSE=刷新
        self.driver = init_driver(True)
        self.page = Page(self.driver)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("version_update_data.yaml", "test_login"))
    def test_login(self, args, page, my_current_activity):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        # 没登录登录
        self.page.home.page_login_if_not(page, my_current_activity, username, password)
        # 点击设置
        self.page.me.click_setting_button()
        # 找到关于奥莱并点击
        self.page.setting.page_setting_scroll_find_click()
        # 点击最新版本
        self.page.setting.click_new_version()
        # 判断提示存在
        self.page.setting.find_toast()
        # 获得提示内容
        self.page.setting.get_toast()



