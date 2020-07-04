import os
import unittest
from time import sleep
from appium import webdriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestCase2(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_wifi_settings(self):
        self.driver.find_element_by_accessibility_id("Preference").click()
        self.driver.find_element_by_accessibility_id(
            "3. Preference dependencies").click()
        checkboxes = self.driver.find_elements_by_android_uiautomator(
            'new UiSelector().checkable(true)')
        for el in checkboxes:
            el.click()
        for el in checkboxes:
            is_checked_value = self.driver.find_element_by_class_name(
                "android.widget.CheckBox").get_attribute("checked")
            if is_checked_value == 'true':
                print("Wszystkie checkboxy są zaznaczone")

        self.driver.find_element_by_xpath("//*[@text='WiFi settings']").click()

        # inne opcje na kliknięcie na "WiFi settings:
        # self.driver.find_element_by_class_name("android.widget.RelativeLayout[2]")
        # self.driver.find_element_by_xpath("android.widget.RelativeLayout"[1])

        sleep(1)
        passwordInput = "1234"
        self.driver.find_element_by_class_name(
            "android.widget.EditText").send_keys(passwordInput)
        sleep(10)
        passwordCurrent = self.driver.find_element_by_class_name(
            "android.widget.EditText").get_attribute("text")

        self.assertEqual(passwordCurrent, passwordInput)

        self.driver.find_element_by_id("android:id/button1").click()

        self.driver.back()
        self.driver.keyevent(4)  # inny sposob na klikij wstecz
        sleep(3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    unittest.TextTestRunner(verbosity=2).run(suite)
