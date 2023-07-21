from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    BREADCRUMB = (By.CLASS_NAME, 'breadcrumb')
    LIST_GROUP = (By.CLASS_NAME, 'list-group')
    LIST_GROUP_ITEMS = (By.CLASS_NAME, 'list-group-item')
    CONTENT = (By.ID, 'content')
    PRODUCT_LAYOUT = (By.CLASS_NAME, 'product-layout')
