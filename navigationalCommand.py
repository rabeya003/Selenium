from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Open Chrome
driver = webdriver.Chrome ()
driver.maximize_window()


driver.get("https://amarsolution.com/")
driver.get("https://www.amazon.com/ref=nav_logo")

driver.back()  # Navigate back to the previous page (amarsolution.com)
driver.forward()  # Navigate forward to the next page (amazon.com)

driver.refresh()  # Refresh the current page (amazon.com)

time.sleep(5)
driver.quit()