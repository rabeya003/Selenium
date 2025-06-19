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
        EC.presence_of_element_located((By.ID, "txtUsername"))
    )   


time.sleep(3)
driver.quit()
