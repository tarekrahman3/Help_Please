from selenium import webdriver
import os
import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
#options.headless = True #(turn on background mode)
driver = webdriver.Chrome(options=options,
          executable_path='chromedriver')   


### {RIJVY}    Eikhan theke main process suru     #####
### {RIJVY}    Chrome webdriver use kore Selenium module google er home page open korbe     #####

driver.get("http://www.google.com")  
time.sleep(6)

### {RIJVY}    google er Search box find korar xpath     #####
que=driver.find_element_by_xpath("//input[@name='q']")

### {RIJVY}    search box e search query likhbe     #####
que.send_keys("Manchester FC Official Website")
time.sleep(6)

### {RIJVY}    Keys.RETURN er maddhome Enter press kore     #####
que.send_keys(Keys.RETURN)
time.sleep(5)

### {RIJVY}    eikhane element hosse search results er prothom result er xpath     #####
element=driver.find_element_by_xpath('//div[2]/div/div[1]/a')

### {RIJVY}    eikhane href hosse first result er href attribute     #####
href = element.get_attribute('href')
print (href)

#driver.quit()
