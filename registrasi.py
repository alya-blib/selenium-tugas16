import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elem
from DataStorage.data import inputan

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success register
    def test_success_register(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH, elem.linkRegister).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaToko).send_keys(inputan.isiNamaToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys(inputan.isiEmailToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.registerButton).click()
        time.sleep(1)

        # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + "login")

    # empty name
    def test_empty_name_register(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH, elem.linkRegister).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaToko).send_keys("")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys(inputan.isiEmailToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.registerButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorMessageName, error_message)
    
    # empty email
    def test_empty_email_register(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH, elem.linkRegister).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaToko).send_keys(inputan.isiNamaToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys("")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.registerButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorMessageEmail, error_message)
    
    # empty password
    def test_empty_password_register(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH, elem.linkRegister).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaToko).send_keys(inputan.isiNamaToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys(inputan.isiEmailToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys("")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.registerButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorMessagePassword, error_message)

     # invalid email
    def test_invalid_email_register(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.XPATH, elem.linkRegister).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaToko).send_keys(inputan.isiNamaToko)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.email).send_keys(inputan.notFormatEmail)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.registerButton).click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorInvalidEmail, error_message)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()