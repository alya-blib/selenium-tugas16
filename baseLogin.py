import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elem

def test_success_login(driver):
    # langkah-langkah
    driver.find_element(By.ID, elem.email).send_keys("alyacake@gmail.com")  # isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys("password")  # isi password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginButton).click()
    time.sleep(1)

