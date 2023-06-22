from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_of_element(browser: WebDriver,
                    element: tuple,
                    time: int = 10) -> None:
    WebDriverWait(browser, time).until(EC.visibility_of_element_located(element))


def wait_and_return_element(browser: WebDriver,
                            element: tuple) -> WebElement:
    return browser.find_element(*element)


def wait_and_return_elements(browser: WebDriver,
                             element: tuple) -> list[WebElement]:
    return browser.find_elements(*element)


def get_text(browser: WebDriver,
             element: tuple) -> str:
    return browser.find_element(*element).text
