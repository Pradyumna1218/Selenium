from selenium.webdriver.common.by import By
import logging

class InventoryPage:
    LOGO_DATA = (By.CLASS_NAME, "app_logo")

    def __init__(self,driver):
        self.driver = driver

    def get_logo(self):
        logo = self.driver.find_element(*self.LOGO_DATA)
        logging.info(f"Logo text:  {logo.text}")
        return logo