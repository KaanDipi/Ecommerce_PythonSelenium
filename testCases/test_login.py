# https://youtu.be/57pjD89IFXA?t=3347

# ----------importing plugs
import pytest
from selenium import webdriver

# ----------importing classes
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

# -------------------------------------------------------------------------------------------------------
    @pytest.mark.regression
    def test_homePageTitle(self,setup): # setup is inside of conftest.py

        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")

# self.driver=webdriver.Chrome()
        self.driver = setup # setup return driver

        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)

        act_title=self.driver.title

        if act_title== "Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle1.png")
            self.driver.close()
            assert False

# --------------------------------------------------------------------------------------------------------

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Login Test****")

# self.driver=webdriver.Chrome()
        self.driver = setup

        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver) # creating an object of LoginPage to access its method
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_test_login1.png")
            self.driver.close()
            assert False

