from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType

class BasePage:

    SPINER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait (driver,10, poll_frequency=0.3)

# чтобы помогать открывать страницы

    def open(self):
        with allure.step(f"Open {self.URL} page"):
            self.driver.get(self.URL) # URL будет подставляться для каждой страницы индивидуально
            self.is_opened()

# проверять открыта ли странциа
    def is_opened(self):
        with allure.step(f"Page {self.URL} is opened"):
            self.wait.until(EC.url_to_be(self.URL))
            self.wait.until(EC.invisibility_of_element(self.SPINER))

    def screenschot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )