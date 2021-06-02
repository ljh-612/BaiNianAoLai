from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class PageLogin(BaseAction):
    username = By.XPATH, "//*[@text = '请输入手机/昵称']"
    password = By.XPATH, "//*[@resource-id = 'com.yunmall.lc:id/logon_password_textview']"
    login_button = By.XPATH, "//*[@text = '登录']"

    # 输入登录用户名
    def page_login_input_username(self, username):
        self.input(self.username, username)

    # 输入登录密码
    def page_login_input_password(self, password):
        self.input(self.password, password)

    # 点击登录
    def page_login(self):
        self.click(self.login_button)

    # 判断toast是否存在
    def page_login_find_toast(self, message):
        self.find_toast(message)

    # 获得toast提示
    def page_login_get_toast(self, message):
        self.get_toast(message)
