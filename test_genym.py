import pytest
from appium import webdriver

@pytest.mark.parametrize("udid, systemPort", [
       ("localhost:30000", "8203"),
       ]
)
def test_sum(udid, systemPort):

   capabilities = {
       'platformName': 'Android',
       'deviceName': 'Genymotion Cloud',
       'appPackage': 'com.android.calculator2',
       'appActivity': '.Calculator',
       'udid':udid,
       'systemPort': systemPort,
       'automationName': 'UiAutomator2',
       'noReset': True,
   }
   url = 'http://localhost:4723/wd/hub'
   driver = webdriver.Remote(url, capabilities)

   try:
       digit1_btn = driver.find_element_by_id("com.android.calculator2:id/digit_1")
       digit1_btn.click()

       add_btn = driver.find_element_by_id("com.android.calculator2:id/op_add")
       add_btn.click()

       digit2_btn = driver.find_element_by_id("com.android.calculator2:id/digit_2")
       digit2_btn.click()

       equal_btn = driver.find_element_by_id("com.android.calculator2:id/eq")
       equal_btn.click()

       sum_input = driver.find_element_by_id("com.android.calculator2:id/result").text
       assert sum_input == "4"

   finally:
       # teardown appium
       driver.quit()
