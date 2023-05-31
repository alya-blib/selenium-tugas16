import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin
from PageObject.locator import elem
from DataStorage.data import inputan

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success add customer
    def test_success_add_customer(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

       # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + inputan.linkDashboard)

        driver.find_element(By.XPATH, elem.linkpelanggan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonTambah).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaKategori).send_keys(inputan.namaPelanggan)  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, elem.noHp).send_keys(inputan.noHpPelanggan)  # isi no hp
        time.sleep(1)
        driver.find_element(By.ID, elem.alamat).send_keys(inputan.alamatPelanggan)  # isi alamat
        time.sleep(1)
        driver.find_element(By.ID, elem.keterangan).send_keys(inputan.keteranganPelanggan)  # isi keterangan
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

        # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + inputan.linkpelanggan)

    # empty name di add customer
    def test_empty_name_add_customer(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get(elem.baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

         # validasi
        url = driver.current_url
        self.assertIn (url, elem.baseUrl + inputan.linkDashboard)

        driver.find_element(By.XPATH, elem.linkpelanggan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.buttonTambah).click()
        time.sleep(1)
        driver.find_element(By.ID, elem.namaKategori).send_keys("")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, elem.noHp).send_keys(inputan.noHpPelanggan)  # isi no hp
        time.sleep(1)
        driver.find_element(By.ID, elem.alamat).send_keys(inputan.alamatPelanggan)  # isi alamat
        time.sleep(1)
        driver.find_element(By.ID, elem.keterangan).send_keys(inputan.keteranganPelanggan)  # isi keterangan
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        time.sleep(1)

       # validasi
        error_message = driver.find_element(By.CLASS_NAME, elem.alert).text
        self.assertEqual(inputan.errorMessageName, error_message)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

