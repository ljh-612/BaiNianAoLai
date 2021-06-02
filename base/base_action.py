from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        """
        根据特征，找元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(feature_by, feature_value))
        return element

    def find_elements(self, feature, timeout=10, poll=1):
        """
        根据特征，找多个符合条件的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        feature_by, feature_value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(feature_by, feature_value))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()

    def get_text(self, feature):
        return self.find_element(feature, 15, 1).text

    # 判断是否存在toast
    def find_toast(self, message):
        toast_message = By.XPATH, "//*[contains(@text, '%s')]" % message
        try:
            self.find_element(toast_message, 15, 1)
            return True
        except TimeoutException:
            return False

    # 获取toast内容
    def get_toast(self, message):
        if self.find_toast(message):
            toast_message = By.XPATH, "//*[contains(@text, '%s')]" % message
            return self.find_element(toast_message).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或者toast有没有出现在屏幕上")

    # 只滑动不找元素的方法
    def only_scroll(self, direction="up"):
        """
        只滑动不找元素
                :param feature:页面元素
                :param page_source:页面源代码
                :param direction: 方向
                            "up":"从下到上"
                            "down":"从上到下"
                            "left":"从右到左"
                            "right":"从左到右"
                :return:
                """
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = 1 * width / 2
        center_y = 1 * height / 2
        left_x = 1 * width / 4
        left_y = center_y
        right_x = 3 * width / 4
        right_y = center_y
        top_x = center_x
        top_y = 1 * height / 4
        bottom_x = center_x
        bottom_y = 3 * height / 4

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        # 传入错误参数抛出异常
        else:
            raise Exception("请检查参数是否正确")

    # 滑动找元素的方法
    def find_element_with_scroll(self, feature, direction="up"):
        """
        边滑边找元素，找到元素后的操作并不固定
        :param feature:页面元素
        :param direction: 方向
                    "up":"从下到上"
                    "down":"从上到下"
                    "left":"从右到左"
                    "right":"从左到右"
        :return:返回元素
        """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.only_scroll(direction)
                if self.driver.page_source == page_source:
                    print("到底了")
                    break

