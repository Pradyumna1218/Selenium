

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options= Options()
    prefs = {"profile.password_manager_leak_detection": False,
         "credentials_enable_service": False,
         "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument("--disable-features=PasswordLeakDetection,PasswordChange,AutofillEnableAccountWalletStorage")
    # options.add_argument("--disable-save-password-bubble")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

