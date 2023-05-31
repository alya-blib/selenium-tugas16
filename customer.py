import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import baseLogin

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success add customer
    def test_success_add_customer(self):
        # langkah-langkah
        baseUrl = 'https://kasirdemo.belajarqa.com/'
        driver = self.browser  # buka web browser
        driver.get(baseUrl)  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

       # validasi
        url = driver.current_url
        self.assertIn (url, baseUrl + "dashboard")

        driver.find_element(By.XPATH, '//a[@href="/customers" or contains(text(), "pelanggan")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[@href="/customers/create" or contains(text(), "tambah")]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("hari")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, "no.hp").send_keys("086372837282")  # isi no hp
        time.sleep(1)
        driver.find_element(By.ID, "alamat").send_keys("cikunir")  # isi alamat
        time.sleep(1)
        driver.find_element(By.ID, "keterangan").send_keys("cari elektronik")  # isi keterangan
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        url = driver.current_url
        self.assertIn (url, baseUrl + "customers")

    # empty name di add customer
    def test_empty_name_add_customer(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(1)
        baseLogin.test_success_login(driver)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME, "chakra-heading").text
        self.assertIn('kasirAja', response_data)

        driver.find_element(By.XPATH, '//a[@href="/customers" or contains(text(), "pelanggan")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[@href="/customers/create" or contains(text(), "tambah")]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, "no.hp").send_keys("086372837282")  # isi no hp
        time.sleep(1)
        driver.find_element(By.ID, "alamat").send_keys("cikunir")  # isi alamat
        time.sleep(1)
        driver.find_element(By.ID, "keterangan").send_keys("cari elektronik")  # isi keterangan
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

       # validasi
        error_message = driver.find_element(By.CLASS_NAME, "chakra-alert").text
        self.assertEqual('"name" is not allowed to be empty', error_message)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

