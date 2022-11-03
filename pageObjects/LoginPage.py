# https://youtu.be/57pjD89IFXA?t=2817

# A class that contains LoginPage objects for test cases.

from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:


# Login Page Objects
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_linktext = "Logout" # this is a linktext, so we can define it with its name

# this is a python constructor, meaning that it automatically is invoked when object created
    def __init__(self,driver): # this driver comes from actual test case
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()  # the link behind text is "en/get-started"
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()