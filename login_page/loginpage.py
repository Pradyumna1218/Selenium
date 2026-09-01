from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_FIELD = (By.ID, 'user-name')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    SYSTEM_URL = "https://www.saucedemo.com"

    def __init__(self,driver):
        self.driver = driver

    def login(self,driver):
        uname_element = self.driver.find_element(*self.USERNAME_FIELD)
        uname_element.send_keys("standard_user")

        password_element = self.driver.find_element(*self.PASSWORD_FIELD)
        password_element.send_keys("secret_sauce")

        login_button_element = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button_element.click()