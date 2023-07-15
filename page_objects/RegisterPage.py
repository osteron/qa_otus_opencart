from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class RegisterPage(BasePage):
    FIRSTNAME_INPUT = (By.NAME, 'firstname')
    LASTNAME_INPUT = (By.NAME, 'lastname')
    EMAIL_INPUT = (By.NAME, 'email')
    TELEPHONE_INPUT = (By.NAME, 'telephone')
    PASSWORD_INPUT = (By.NAME, 'password')
    CONFIRM_PASSWORD_INPUT = (By.NAME, 'confirm')
    AGREE_CHECKBOX = (By.CSS_SELECTOR, 'input[name=agree]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type=submit]')
    ACCOUNT_CREATED = (By.CSS_SELECTOR, '#content h1')
    REGISTER_TEXT = 'Your Account Has Been Created!'

    def register(self, firstname, lastname, email, telephone, password):
        self._input(self.element(self.FIRSTNAME_INPUT), firstname)
        self._input(self.element(self.LASTNAME_INPUT), lastname)
        self._input(self.element(self.EMAIL_INPUT), email)
        self._input(self.element(self.TELEPHONE_INPUT), telephone)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self._input(self.element(self.CONFIRM_PASSWORD_INPUT), password)
        self.click(self.element(self.AGREE_CHECKBOX))
        self.click(self.element(self.SUBMIT_BUTTON))
        return self

    def validate_register(self) -> bool:
        return self.get_text_of_element(self.ACCOUNT_CREATED) in self.REGISTER_TEXT
