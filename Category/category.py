import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # success add category
    def test_success_add_category(self):
        # langkah-langkah
        baseUrl = 'https://kasirdemo.belajarqa.com/'
        driver = self.browser  # buka web browser
        driver.get(baseUrl)  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("alyacake@gmail.com")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("password")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        url = driver.current_url
        self.assertIn (url, baseUrl + "dashboard")

        driver.find_element(By.XPATH, '//a[@href="/categories" or contains(text(), "kategori")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[@href="/categories/create" or contains(text(), "tambah")]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("elektronik")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, "deskripsi").send_keys("semua nya ada garansi")  # isi deskripsi
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        url = driver.current_url
        self.assertIn (url, baseUrl + "categories")

    # empty name di add category
    def test_empty_name_add_category(self):
        # langkah-langkah
        driver = self.browser  # buka web browser
        driver.get("https://kasirdemo.belajarqa.com/")  # buka situs
        time.sleep(1)
        driver.find_element(By.ID, "email").send_keys("alyacake@gmail.com")  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys("password")  # isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "chakra-button").click()
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME, "chakra-heading").text
        self.assertIn('kasirAja', response_data)

        driver.find_element(By.XPATH, '//a[@href="/categories" or contains(text(), "kategori")]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//a[@href="/categories/create" or contains(text(), "tambah")]').click()
        time.sleep(1)
        driver.find_element(By.ID, "nama").send_keys("")  # isi nama
        time.sleep(1)
        driver.find_element(By.ID, "deskripsi").send_keys("semua nya ada garansi")  # isi deskripsi
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
