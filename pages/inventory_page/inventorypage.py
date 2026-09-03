from selenium.webdriver.common.by import By
import logging

class InventoryPage:
    LOGO_DATA = (By.CLASS_NAME, "app_logo")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_label")
    ITEM_DESC_PARENT = (By.CLASS_NAME, "inventory_item_description")
    ITEM_TITLE = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self,driver):
        self.driver = driver


    def get_logo(self):
        logo = self.driver.find_element(*self.LOGO_DATA)
        logging.info(f"Logo text:  {logo.text}")
        return logo

    def get_item_name(self):
        item_element = self.driver.find_elements(*self.ITEM_NAME)
        for item in item_element:
            logging.info(f"Item name:  {item.text}")

    def get_item_title_price(self):
        parent_element = self.driver.find_elements(*self.ITEM_DESC_PARENT)
        item_list = []
        for parent in parent_element:
            item = []
            title = parent.find_element(*self.ITEM_TITLE)
            price = parent.find_element(*self.ITEM_PRICE)
            logging.info(f"Item title:  {title.text}  price: {price.text}")

            item.append(title.text)
            item.append(price.text)
            item_list.append(item)
        return item_list
