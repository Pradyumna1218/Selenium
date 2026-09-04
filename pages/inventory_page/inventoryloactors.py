from selenium.webdriver.common.by import By

class InventoryLocators:
    LOGO_DATA = (By.CLASS_NAME, "app_logo")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_label")
    ITEM_DESC_PARENT = (By.CLASS_NAME, "inventory_item_description")
    ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")