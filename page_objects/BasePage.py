from selenium.webdriver import ActionChains
from typing import AnyStr, List
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, element) -> None:
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value) -> None:
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple) -> WebElement:
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Не дождался видимости элемента {locator}')

    def elements(self, locator: tuple) -> List[WebElement]:
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f'Не дождался видимости элементов {locator}')

    def get_text_of_element(self, locator: tuple) -> AnyStr:
        return self.element(locator).text

    def check_title_page(self, title: str) -> bool:
        return self.driver.title in title