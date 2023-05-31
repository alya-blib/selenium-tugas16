import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.locator import elem
from DataStorage.data import inputan

def test_success_login(driver):
    # langkah-langkah
    driver.find_element(By.ID, elem.email).send_keys(inputan.validEmail)  # isi email
    time.sleep(1)
    driver.find_element(By.ID, elem.password).send_keys(inputan.validPassword)  # isi password
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, elem.loginButton).click()
    time.sleep(1)

