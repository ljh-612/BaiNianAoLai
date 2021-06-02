from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class PageRegister(BaseAction):
    go_login_button = By.XPATH, "//*[@text = '已有账号，去登录']"
    register_button = By.XPATH, "//*[@text = '手机号注册']"

    # 点击去登录
    def page_go_login(self):
        self.click(self.go_login_button)

    # 点击去注册
    def page_register(self):
        self.click(self.register_button)