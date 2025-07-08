from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Open Chrome
driver = webdriver.Chrome ()
driver.maximize_window()
# 2. Go to login page
driver.get("https://demo.nopcommerce.com/register")

#is_displayed() - to check if an element is visible on the page
# is_enabled() - to check if an element is enabled (clickable)  
searchhBox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",searchhBox.is_displayed())
print("Enabled status:",searchhBox.is_enabled())

#is_selected() -for radio buttons and check boxes
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click() # selecting male radio button..
print("After selecting male radio button .....")
print(rd_male.is_selected()) # True
print(rd_female.is_selected()) # False
time.sleep(2) 

rd_female.click() # selecting male radio button..
print("After selecting Female radio button .....")
print(rd_male.is_selected()) # false
print(rd_female.is_selected()) # true


# 6. Close browser after 20 seconds
time.sleep(20)
driver.quit()