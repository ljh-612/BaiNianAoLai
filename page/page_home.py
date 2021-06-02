from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class PageHome(BaseAction):
    home_button = By.XPATH, "//*[@text = '我']"

    # 点击我
    def page_home_click_me(self):
        self.click(self.home_button)

    def page_login_if_not(self, page, my_current_activity, username, password):
        # 判断登录状态
        self.page_home_click_me()
        if self.driver.current_activity != my_current_activity:
            return
        # 没有登录就登录
        # 输入用户名
        page.login.page_login_input_username(username)
        # 输入密码
        page.login.page_login_input_password(password)
        # 点击登录
        page.login.page_login()
