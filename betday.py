import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from decouple import config

driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.maximize_window()
driver.get("https://www.betpawa.ug")
driver.find_element(by=By.CSS_SELECTOR, value='a[href="/login"]').click()
time.sleep(5)
driver.find_element(by=By.CSS_SELECTOR, value='#login-form-phoneNumber').send_keys('775236691')
driver.find_element(by=By.CSS_SELECTOR, value='#login-form-password').send_keys('34454392')
driver.find_element(by=By.CSS_SELECTOR, value='input[value="Log In"]').click()
time.sleep(10)
driver.get('https://www.betpawa.ug/popular')
time.sleep(10)
matches = driver.find_elements(by=By.CLASS_NAME, value='events-container.prematch')
time.sleep(100)
# driver.close()