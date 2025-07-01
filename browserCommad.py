from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Open Chrome
driver = webdriver.Chrome ()
# 2. Go to login page
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
)   

time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

time.sleep(5)
driver.quit()
# driver.close()