from selenium.webdriver.common.by import By


class RegisterSelectors:
    personal_details_inputs = (By.CSS_SELECTOR, '.form-group.required')
    radio_inlines = (By.CLASS_NAME, 'radio-inline')
    agree_checkbox = (By.NAME, 'agree')
    submit = (By.CSS_SELECTOR, '.btn.btn-primary')
    column_right = (By.CSS_SELECTOR, '.list-group a')
