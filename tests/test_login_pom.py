import time

from login_page.loginpage import LoginPage
from inventory.inventorypage import InventoryPage

def test_login_flow(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.SYSTEM_URL)
    login_page.login(driver)
    time.sleep(2)

    inventory_page = InventoryPage(driver)

    logo = inventory_page.get_logo()
    assert logo.text == "Swag Labs"


