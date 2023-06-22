from selenium.webdriver.common.by import By


class CatalogSelectors:
    breadcrumb = (By.CLASS_NAME, 'breadcrumb')
    list_group = (By.CLASS_NAME, 'list-group')
    list_group_items = (By.CLASS_NAME, 'list-group-item')
    content = (By.ID, 'content')
    product_layout = (By.CLASS_NAME, 'product-layout')
