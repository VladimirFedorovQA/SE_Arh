import time

from selenium.webdriver.support.expected_conditions import new_window_is_opened
import allure
from base.base_page import BasePage # чтобы пробрасывать общие методы для всех страницы
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys

class PersonalPage(BasePage):
    URL = Links.PERSONAL_PAGE

    FIRSTNAME_INPUT = ("xpath", "//input[@name='firstName']")
    SUBMIT_BUTTON = ("xpath","//button[@type='submit']")


    def change_name(self, new_name):
        with (allure.step(f"change_name on '{new_name}'")):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRSTNAME_INPUT) )
            first_name_field.click()
            i=0
            while i in range(len(first_name_field.get_attribute("value"))):
                first_name_field.send_keys(Keys.BACK_SPACE)
                i+=i
            assert first_name_field.get_attribute("value")=="", "FirstName input is not cleared"
            first_name_field.click()
            first_name_field.send_keys(new_name)
            self.new_name=new_name

    @allure.step("save_changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
        self.is_opened()

    @allure.step("save_changes - is_saved")
    def is_saved(self):
        #self.wait.until(EC.invisibility_of_element_located(self.SPINER))
        self.wait.until(EC.visibility_of_element_located(self.FIRSTNAME_INPUT))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRSTNAME_INPUT, self.new_name)) # тут типа он будет ждать появления