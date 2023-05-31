import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_success_login(driver):
    # langkah-langkah
    baseUrl = 'https://kasirdemo.belajarqa.com/'
    driver.get(baseUrl)  # buka situs
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("alyacake@gmail.com")  # isi email
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("password")  # isi password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, "chakra-button").click()
    time.sleep(1)

