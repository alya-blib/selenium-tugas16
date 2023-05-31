import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success login
    def test_success_login(self):
        # langkah-langkah
        baseUrl = 'https://kasirdemo.belajarqa.com/'
        driver = self.browser  # buka web browser
        driver.get(baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

        # validasi
        url = driver.current_url
        self.assertIn (url, baseUrl + "dashboard")

    # test invalid email
    def test_invalid_email_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("invalidemail@gmail.com")  # isi email yang salah
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("password")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, "chakra-alert").text
        self.assertEqual("Kredensial yang Anda berikan salah", error_message)

    # test empty email
    def test_empty_email_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("")  # email kosong
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("password")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, "css-qwanz3").text
        self.assertEqual('"email" is not allowed to be empty', error_message)

     # test empty password
    def test_empty_password_login(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("alyacake@gmail.com")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("")  # password kosong
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        error_message = driver.find_element(By.CLASS_NAME, "chakra-alert").text
        self.assertEqual('"password" is not allowed to be empty', error_message)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()