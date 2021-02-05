import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestForm(unittest.TestCase):
    def setUp(self):
        chromeDriverLoc = 'E:/chromedriver'
        self.driver = webdriver.Chrome(chromeDriverLoc)

    def test_HW_user_input(self):
        driver = self.driver
        driver.get("https://forms.liferay.com/web/forms/shared/-/form/122548")
        time.sleep(2)

        elem = driver.find_element_by_xpath('//*[contains(@name, "WhatIsYourName")]')
        elem.send_keys("naief")
        time.sleep(0.5)
        
        elem = driver.find_element_by_xpath('//*[contains(@class, "form-control input-group-inset input-group-inset-after")]')
        elem.send_keys(Keys.HOME)        
        elem.send_keys("07101990")
        time.sleep(0.5)

        elem = driver.find_element_by_xpath('//*[contains(@name, "WhyDidYouJoinTheTestingArea")]')
        elem.send_keys("naief bitar")
        time.sleep(0.5)

        elem = driver.find_element_by_xpath('//*[contains(@type, "submit")]')
        elem.click()

        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[contains(@class, "ddm-form-name")]')
        text1 = elem.get_attribute("innerHTML")
        self.assertIn("Information sent",text1)

    def test_EW_required(self):
        driver = self.driver
        driver.get("https://forms.liferay.com/web/forms/shared/-/form/122548")
        time.sleep(2)

        elem = driver.find_element_by_xpath('//*[contains(@type, "submit")]')
        elem.click()
        time.sleep(2)
        #assertion of the name field error msg
        elem = driver.find_element_by_xpath('(//*[contains(@class, "form-feedback-item help-block")])[1]')
        text1 = elem.get_attribute("innerHTML")
        self.assertIn("This field is required.",text1)
        
        #assertion of the date of birth field error msg
        elem = driver.find_element_by_xpath('(//*[contains(@class, "form-feedback-item help-block")])[2]')
        text2 = elem.get_attribute("innerHTML")
        self.assertIn("This field is required.",text1)
        
        #assertion of the text area field error msg
        elem = driver.find_element_by_xpath('(//*[contains(@class, "form-feedback-item help-block")])[3]')
        text3 = elem.get_attribute("innerHTML")
        self.assertIn("This field is required.",text1)

    def test_err_futuredate(self):
        driver = self.driver
        driver.get("https://forms.liferay.com/web/forms/shared/-/form/122548")
        time.sleep(2)

        elem = driver.find_element_by_xpath('//*[contains(@name, "WhatIsYourName")]')
        elem.send_keys("naief")
        time.sleep(0.5)
        
        elem = driver.find_element_by_xpath('//*[contains(@class, "form-control input-group-inset input-group-inset-after")]')
        elem.send_keys(Keys.HOME)        
        elem.send_keys("07102021")
        time.sleep(0.5)

        elem = driver.find_element_by_xpath('//*[contains(@name, "WhyDidYouJoinTheTestingArea")]')
        elem.send_keys("naief bitar")
        time.sleep(0.5)

        elem = driver.find_element_by_xpath('//*[contains(@type, "submit")]')
        elem.click()
        time.sleep(2)

        elem = driver.find_element_by_xpath('(//*[contains(@class, "form-feedback-item help-block")])[1]')
        text1 = elem.get_attribute("innerHTML")
        self.assertIn("The date should't be in the future",text1)


if __name__ == '__main__':
    unittest.main()
