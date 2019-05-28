import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller

driver = webdriver.Firefox()
driver.get("http://whale.hacking-lab.com:3555")
wait = WebDriverWait(driver,10)
count = 0
while count < 42:
    #if screenshot doesn't work we have to download the picture
    #img = driver.find_element_by_id('img1')
    #src = img.get_attribute('src')
    #img = requests.get(src)
    #with open('picture.jpg', 'wb') as f:
    #    f.write(img.content)
   
    #get screenshot    
    time.sleep(2)
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "img1")))
    driver.get_screenshot_as_file("picture.png")
    
    #maybeconversion to jpg with convert is necesairy

    #Write Number to field 
    elem2 = driver.find_element_by_id("s")
    elem2.clear()
    Eggs = len(KeyPoints) #
    elem2.send_keys(Eggs)
    elem2.send_keys(Keys.RETURN)
