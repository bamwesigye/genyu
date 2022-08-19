from datetime import datetime
import time, sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from decouple import config


options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

conn = sqlite3.connect('betpawa.db')
print("Opened database successfully")


driver.maximize_window()
driver.get("https://www.betpawa.ug")
driver.find_element(by=By.CSS_SELECTOR, value='a[href="/login"]').click()
time.sleep(2)
driver.find_element(by=By.CSS_SELECTOR, value='#login-form-phoneNumber').send_keys(config('BETPAWA_USERNAME'))
driver.find_element(by=By.CSS_SELECTOR, value='#login-form-password').send_keys(config('BETPAWA_PASSWORD'))
time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR, value='input[value="Log In"]').click()
time.sleep(5)
driver.get('https://www.betpawa.ug/popular')
time.sleep(2)
matches = driver.find_elements(by=By.CLASS_NAME, value='events-container.prematch')
for match in matches:
    event = match.text.split('\n')
    event_link = match.find_element(by=By.CSS_SELECTOR, value='a[class="event-match"]').get_attribute('href')
    print("Event Link = ",event_link)
    event_time = datetime.strptime(event[0]+' '+ str(datetime.strftime(datetime.now(),'%Y')),'%H:%M %p %a %d/%m %Y')
    print(event[5])
    print(event_time)
    try:
        conn.execute("INSERT INTO events (event_link, competition, event_time, home_team, away_team, home_odds, draw_odds, away_odds) VALUES (?,?,?,?,?,?,?,?)",(event_link, event[3], event_time, event[1], event[2], event[5], event[7],event[9]))
        conn.commit()
    except:
        print("Error")
        conn.execute("UPDATE events SET competition = ?, event_time = ?, home_team = ?, away_team = ?, home_odds = ?, draw_odds = ?, away_odds = ? WHERE event_link = ?",(event[3], event_time, event[1], event[2], event[5], event[7],event[9], event_link))
        conn.commit()

conn.close
    
# driver.close()