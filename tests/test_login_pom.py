import logging
import time


from pages.login_page.loginpage import LoginPage
from pages.inventory_page.inventorypage import InventoryPage

def test_login_flow(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.SYSTEM_URL)
    login_page.login(driver)
    time.sleep(2)

    inventory_page = InventoryPage(driver)

    logo = inventory_page.get_logo()
    assert logo.text == "Swag Labs"

def test_inventory_item(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.SYSTEM_URL)
    login_page.login(driver)

    inv_page = InventoryPage(driver)
    item_page = inv_page.get_item_name()
    item_title_price_list = inv_page.get_item_title_price()
    assert item_title_price_list[0][0] == "Sauce Labs Backpack"






