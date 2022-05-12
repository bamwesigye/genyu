from datetime import datetime
from os import link
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from decouple import config
import sqlite3

conn = sqlite3.connect('betpawa.db')
print("Opened database successfully")

def bplogin(driver):
    driver.get("https://www.betpawa.ug/login")
    # driver.find_element(by=By.CSS_SELECTOR, value='a[href="/login"]').click()
    time.sleep(5)
    driver.find_element(by=By.CSS_SELECTOR, value='#login-form-phoneNumber').send_keys(config('BETPAWA_USERNAME'))
    driver.find_element(by=By.CSS_SELECTOR, value='#login-form-password').send_keys(config('BETPAWA_PASSWORD'))
    time.sleep(1)
    driver.find_element(by=By.CSS_SELECTOR, value='input[value="Log In"]').click()
    time.sleep(10)
    return driver

def bplive(driver):
    driver.get('https://www.betpawa.ug/live')
    time.sleep(10)
    matches = driver.find_elements(by=By.CLASS_NAME, value='events-container.prematch')
    for matchno, match in enumerate(matches):
        event_link = match.find_element(by=By.CSS_SELECTOR, value='a[class="event-match"]').get_attribute('href')
        print("matchno= ",matchno,"   =   Event Link = ",event_link, "\n",match.text,"\n\n\n\n")

    select_match = int(input("Enter a matchno: "))
    print("selected match = ",select_match)
    selected_link = matches[select_match].find_element(by=By.CSS_SELECTOR, value='a[class="event-match"]').get_attribute('href')
    driver.get(selected_link)
    time.sleep(2)
    match_title = driver.find_element(by=By.CLASS_NAME, value='live-event')
    print(match_title.text)
    #get minutes current
    match_score = match_title.find_elements(by = By.CLASS_NAME, value='live-event-score')
    match_score = match_score.split('/n')



driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.maximize_window()
if __name__ == "__main__":
    bplive(driver=driver)
    
# driver.close()