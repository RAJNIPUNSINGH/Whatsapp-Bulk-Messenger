from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

login_time = 30
new_msg_time = 5
send_msg_time = 5
country_code = 91

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

with open('message.txt', 'r') as file:
    msg = file.read()

link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)
        
driver.quit()