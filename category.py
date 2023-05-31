import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from PageObject.locator import elem

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success add category
    def test_success_add_category(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

        # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + "dashboard")

        driver.find_element(By.XPATH, elem.linkKategoi).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonTambah).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaKategori).send_keys("elektronik")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, elem.deskripsi).send_keys("semua nya ada garansi")  # isi deskripsi
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

        # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + "categories")

    # empty name di add category
    def test_empty_name_add_category(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

        # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + "dashboard")

        driver.find_element(By.XPATH, elem.linkKategoi).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonTambah).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaKategori).send_keys("")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, elem.deskripsi).send_keys("semua nya ada garansi")  # isi deskripsi
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

       # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual('"name" is not allowed to be empty', error_message)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
