from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time

class StatesList(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
        chrome_driver = "/Users/donniewalker/PycharmProjects/lib/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        self.base_url = "https://test.salesforce.com"

    def test_state_field_populates(self):
        driver = self.driver
        driver.get(self.base_url)

        window_before = driver.window_handles[0]
        print(window_before)

        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test-ug6swfcwdsa5@example.com")
        driver.find_element_by_id("password").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("28)Gg#kH|G")
        driver.find_element_by_id("Login").click()

        element1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, "//*[@id='66:195;a']/div/div/a")))
        element1.click()
        element2 = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='related_setup_app_home']/a")))
        element2.click()

        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        print(window_after)

        element3 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='split-left']//li[5]//a[contains(text(),'Data')]")))
        element3.click()
        element4 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((
            By.XPATH, "//*[@id='split-left']//a[contains(text(),'State and Country')]")))
        element4.click()

        time.sleep(5)
        driver.switch_to.frame(0)
        element5 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((
            By.ID, "addressCleaner:form:enableBlock:step0ConfigLink")))
        element5.click()

        country = range(0,238)
        count = 9
        for i in country:
            driver = self.driver
            time.sleep(3)
            driver.switch_to.frame(0)
            element6 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
                By.ID, "configstatecountry:form:j_id34:configStateCountryRelList:list:table:%s:editLink" % count)))
            element6.click()

            time.sleep(3)
            driver.switch_to.frame(0)
            element7 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.ID, "configurecountry:form:stateRelatedListComponent:configStateCountryRelList:list:j_id50:buttonAddNew")))
            element7.click()

            time.sleep(5)
            driver.switch_to.frame(0)
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:nameSectionItem:editName").click()
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:nameSectionItem:editName").clear()
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:nameSectionItem:editName").send_keys(
                "Not Applicable")
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:codeSectionItem:editIsoCode").click()
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:codeSectionItem:editIsoCode").clear()
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:codeSectionItem:editIsoCode").send_keys("NA")
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:activeSectionItem:editActive").click()
            time.sleep(3)
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id9:visibleSectionItem:editVisible").click()
            driver.find_element_by_id("configurenew:j_id1:blockNew:j_id43:addButton").click()

            time.sleep(5)
            driver.switch_to.frame(0)
            element7 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
                (By.ID,
                 "configurecountry:form:blockBottomButtons:j_id60:cancelButtonBottom")))
            element7.click()

            time.sleep(5)
            if i <= 238:
                count += 1
        return count

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()