from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Open Chrome
driver = webdriver.Chrome ()
# 2. Go to login page
driver.get("https://opensource-demo.orangehrmlive.com")
print("Page title is:", driver.title)
print("Current URL is:", driver.current_url)
print("Page source is:", driver.page_source)


# 6. Close browser after 20 seconds
time.sleep(20)
driver.quit()