

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options= Options()

    prefs = {"profile.password_manager_leak_detection": False,
         "credentials_enable_service": False,
         "profile.password_manager_enabled": False}
    # options.add_argument("--headless")
    options.add_experimental_option("prefs", prefs)


    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

