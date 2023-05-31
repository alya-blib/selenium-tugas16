import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elem
from DataStorage.data import inputan
import baseLogin

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success login
    def test_success_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

        # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + inputan.linkDashboard)

    # test invalid email
    def test_invalid_email_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys(inputan.invalidEmail)  # isi email yang salah
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorKredensial, error_message)

    # test empty email
    def test_empty_email_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys("")  # email kosong
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alertEmtyMail).text
        self.assertEqual(inputan.errorMessageEmail, error_message)

     # test empty password
    def test_empty_password_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys(inputan.validEmail)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys("")  # password kosong
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorMessagePassword, error_message)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()