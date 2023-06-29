# chromedriver download link:
# https://drive.google.com/file/d/1A8SO8rOofw8K0GXTyF5s5ZI7CVAbAdL4/view?usp=sharing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('https://google.com')

search = driver.find_element('name', 'q')

search.send_keys('MustafaLotfi github')

search.send_keys(Keys.RETURN)

time.sleep(20)