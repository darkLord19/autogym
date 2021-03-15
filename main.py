# import webdriver 
from selenium import webdriver
# import keys
from selenium.webdriver.common.keys import Keys

import time

# create webdriver object 
driver = webdriver.Firefox()

# get gym registration website
driver.get('https://iiscgym.iisc.ac.in/gfr/home.php')

# login to gym registration website
email = driver.find_element_by_id('email')
email.send_keys('chinmayg@iisc.ac.in')

password = driver.find_element_by_id('pass')
password.send_keys('chinmay123')

login = driver.find_element_by_id('login')
login.send_keys(Keys.ENTER)

# sleep for half second so page is loaded fully
time.sleep(0.5)

# click on Self
actor = driver.find_element_by_xpath('//div[@id="deps"]/label')
actor.click()

# choose gymnasium
gymnasium = driver.find_element_by_xpath('//div[@id="fac_rad_grp"]/label[contains(text(), "Gymnasium")]')
gymnasium.click()

# choose slot
slot = driver.find_element_by_id('07')
slot.click()

# submit
book = driver.find_element_by_id('btn_chk')
book.click()