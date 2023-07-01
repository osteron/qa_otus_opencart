from selenium.webdriver.common.by import By


class RegisterSelectors:
    radio_inlines = (By.CLASS_NAME, 'radio-inline')
    agree_checkbox = (By.NAME, 'agree')
    submit = (By.CSS_SELECTOR, '.btn.btn-primary')
    column_right = (By.CSS_SELECTOR, '.list-group a')
