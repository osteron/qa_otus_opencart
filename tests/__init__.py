from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List


IP_ADDRESS = 'http://10.16.49.34'  # paste your local ip address


def wait_and_return_element(browser: WebDriver,
                            element: tuple,
                            time: int = 10) -> WebElement:
    WebDriverWait(browser, time).until(EC.visibility_of_element_located(element))
    return browser.find_element(*element)


def wait_and_return_elements(browser: WebDriver,
                             element: tuple,
                             time: int = 10) -> List[WebElement]:
    WebDriverWait(browser, time).until(EC.visibility_of_all_elements_located(element))
    return browser.find_elements(*element)


def get_text(browser: WebDriver,
             element: tuple) -> str:
    return browser.find_element(*element).text
