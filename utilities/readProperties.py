# https://www.youtube.com/watch?v=y2Kz3QaZcVo
# to read config.ini file
# used for reading common data and re-usability

#  to read data from .ini file, we need to set up some settings
import configparser
config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

# thanks to staticmethod,
# we can access the methods(getApplicationURL etc.) directly by using class name and without creating an object
# have a look at test_login> Test_001_Login
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password