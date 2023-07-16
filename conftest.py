import pytest
import os

from selenium import webdriver

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--url", "-U", default="http://localhost:8081")


@pytest.fixture(scope='session')
def browser(request):
    """ Фикстура инициализации браузера """
    url = request.config.getoption("--url")

    driver = webdriver.Chrome()

    request.addfinalizer(driver.quit)

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)

    return driver
