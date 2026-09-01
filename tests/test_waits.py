import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from first_test import test_sauce_login

@pytest.mark.ui
def test_login_waits(driver):
    test_sauce_login(driver)
    # hard wait
    # time.sleep(5);

    #implicit wait
    # driver.implicitly_wait(10)

    #explicit waits
    # wait = WebDriverWait(driver,1)
    # wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")))

    logo = driver.find_element(By.CLASS_NAME,"app_logo")
    assert logo.is_displayed()
    assert logo.text == "Swag Labs"
    logging.info(f"Logo text:  {logo.text}")
