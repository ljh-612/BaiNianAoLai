from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class PageSetting(BaseAction):
    scroll_find_button = By.XPATH, ""
    new_version_button = By.XPATH, ""

    # 设置页面边滑边找元素并点击
    def page_setting_scroll_find_click(self):
        return self.find_element_with_scroll(self.scroll_find_button).click
    def click_new_version(self):
        self.click(self.new_version_button)




