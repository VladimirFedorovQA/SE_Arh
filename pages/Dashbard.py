import allure

from base.base_page import BasePage # чтобы пробрасывать общие методы для всех страницы
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):
    URL = Links.DASHBOARD_PAGE

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

    @allure.step("Click on link 'My Info'")
    def clik_my_info(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()