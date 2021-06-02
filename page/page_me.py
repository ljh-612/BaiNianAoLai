from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class PageMe(BaseAction):
    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    setting_button = By.XPATH, ""

    # 获得昵称
    def get_nick_name_text_view(self):
        self.get_text(self.nick_name_text_view)

    # 点击设置
    def click_setting_button(self):
        self.click(self.setting_button)