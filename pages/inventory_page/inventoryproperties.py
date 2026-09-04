from conftest import driver
from pages.inventory_page.inventoryloactors import InventoryLocators


class InventoryProperties:

    @property
    def logo(self):
        return self.driver.find_element(*InventoryLocators.LOGO_DATA)

    @property
    def item(self):
        return self.driver.find_elements(*InventoryLocators.ITEM_NAME)

    @property
    def item_desc_parent(self):
        return self.driver.find_elements(*InventoryLocators.ITEM_DESC_PARENT)

    @property
    def item_title(self):
        return self.driver.find_elements(*InventoryLocators.ITEM_TITLE)

    @property
    def item_price(self):
        return self.driver.find_element(*InventoryLocators.ITEM_PRICE)