import pytest

from config.data import Data
from pages.login import LoginPage
from pages.Dashbard import DashboardPage
from pages.Persanal import PersonalPage

class BaseTest:
    data: Data
    login_page=LoginPage
    dashboard_page = DashboardPage
    personal_page = PersonalPage

# инициализирцем все страницы, чтобы они были доступны во всех тестах
    @pytest.fixture(autouse=True)
    def setup(self, request, drv):
        request.cls.drv = drv
        request.cls.data = Data()
        # создаем объекты страниц
        request.cls.login_page = LoginPage(drv)
        request.cls.dashboard_page = DashboardPage(drv)
        request.cls.personal_page = PersonalPage(drv)