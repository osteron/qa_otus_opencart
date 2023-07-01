from selenium.webdriver.common.by import By


class AdminSelectors:
    header_logo = (By.ID, 'header-logo')
    center_panel = (By.CLASS_NAME, 'panel-default')
    panel_title = (By.XPATH, '//h1[@class="panel-title"]/i')
    username_label = (By.XPATH, '//label[@for="input-username"]')
    username_input = (By.ID, 'input-username')
    password_label = (By.XPATH, '//label[@for="input-password"]')
    password_input = (By.ID, 'input-password')
    forgotten_password = (By.CLASS_NAME, 'help-block')
    submit = (By.CSS_SELECTOR, '.btn.btn-primary i')
