"""
@author: Donnie Walker
@email: donalddeanwalker@gmail.com
@date: 18-Feb-27
"""

import logging
import unittest

from base import WebDriver
from pages.loginpage.loginsalesforcepage import LoginPage
from pages.formpage.formjointpage import FormJointPage

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.webdriver_instance = WebDriver()
        cls.webdriver_instance.get_salesforce_webdriver_instance()
        cls.driver = cls.webdriver_instance.driver
        log_in = LoginPage(cls.driver)
        log_in.login_page("test-ctbawsg8setw@example.com", "y$9lB0|YDD")

    def test_submit_form(self):
        logging.info("##### BEGIN SUBMIT FULL FORM #####")
        submit_full_joint_form = FormJointPage(self.driver)
        submit_full_joint_form.submit_form_all("Edgar", "Ed", "Santana", "1234 Yorktown St", "New Hampshire", "67567",
                                         "3546789876", "edgar@santana.com")

    @classmethod
    def tearDownClass(cls):
        logging.info("##### TEARDOWN TEST #####")
        if cls.driver is not None:
            logging.info("# Removing Webdriver #")
            cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
