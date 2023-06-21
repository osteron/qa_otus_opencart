from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_of_element(browser: object, element: tuple):
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(element))


def wait_and_return_elements(browser, element: tuple):
    return browser.find_elements(*element)
