from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.inventory_page.inventoryloactors import InventoryLocators
from pages.inventory_page.inventoryproperties import InventoryProperties


class InventoryPage(InventoryProperties):
    # LOGO_DATA = (By.CLASS_NAME, "app_logo")
    # ITEM_NAME = (By.CLASS_NAME, "inventory_item_label")
    # ITEM_DESC_PARENT = (By.CLASS_NAME, "inventory_item_description")
    # ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    # ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def get_logo(self):
        self.wait.until(expected_conditions.visibility_of_element_located(InventoryLocators.LOGO_DATA))
        # logo = self.driver.find_element(*self.LOGO_DATA)
        title = self.logo
        return title


    def get_item_name(self):
        item_element = self.item
        for item in item_element:
            logging.info(f"Item name:  {item.text}")

    def get_item_title_price(self):
        parent_element = self.item_desc_parent
        item_list = []
        for parent in parent_element:
            item = []
            title = parent.find_element(*InventoryLocators.ITEM_TITLE)
            price = parent.find_element(*InventoryLocators.ITEM_PRICE)
            logging.info(f"Item title:  {title.text}  price: {price.text}")

            item.append(title.text)
            item.append(price.text)
            item_list.append(item)
        return item_list
