from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

import time

# 1. Open Chrome
driver = webdriver.Chrome ()
driver.maximize_window()

# 2. Navigate to the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")


# 3. Wait for the login form to be present
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )   

#4. Enter username and password
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2) 
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

time.sleep(5)
driver.quit()
