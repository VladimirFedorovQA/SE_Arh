import random
import allure
import pytest
from base.base_test import BaseTest # благодаря этому мы можем использовать все объекты страниц через 1 импорт


@allure.feature("Profile")
class TestProfileFeature(BaseTest):

    @allure.title("Change user firstname")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSW)
        self.login_page.submit_by_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.clik_my_info()
        self.personal_page.is_opened()
        self.personal_page.change_name(f"Test {random.randint(1, 100)}")
        self.personal_page.save_changes()
        self.personal_page.is_saved()
        self.personal_page.screenschot("Success")