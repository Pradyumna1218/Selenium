import time

import logging

import pytest
from _pytest import mark
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_get_google(driver):
    driver.get('https://google.com')
    time.sleep(5)


def test_sauce_login(driver):
    driver.get('https://www.saucedemo.com/')

    username = driver.find_element(By.ID, 'user-name')
    username.send_keys('standard_user')

    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')

    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_sauce_info(driver):
    driver.get('https://www.saucedemo.com/')
    credentials = driver.find_element(By.CLASS_NAME, 'login_credentials_wrap-inner')
    text = credentials.text
    logging.info(text)
