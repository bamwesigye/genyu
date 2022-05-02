import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
# # selenium 3 
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=30).install()) 
driver.get("https://www.betpawa.ug")
driver.find_element(by=By.CSS_SELECTOR, value='a[href="/login"]').click()
time.sleep(5)
driver.find_element(by=By.CSS_SELECTOR, value='#login-form-phoneNumber').send_keys('775236691')
driver.find_element(by=By.CSS_SELECTOR, value='#login-form-password').send_keys('34454392')
driver.find_element(by=By.CSS_SELECTOR,value='input[value="Log In"]').click()
time.sleep(10)
# driver.close()