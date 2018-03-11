import unittest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.page.home_page import LoginPage
from utils.config import Config
from utils.config import DRIVER_PATH

OPTION = DRIVER_PATH + '\chromedriver.exe'
c = Config()
URL = c.get('URL')
USR = c.get('product_env')['usr']
PWD = c.get('product_env')['pwd']


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=OPTION)
        self.url = URL
        self.name = USR
        self.pwd = PWD

        login_page = LoginPage(self.driver)
        login_page.login(self.url, self.name, self.pwd)
        WebDriverWait(self.driver, 30).until(EC.title_is(u"我的工作台"))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


