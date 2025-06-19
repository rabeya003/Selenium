from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Open Chrome
driver = webdriver.Firefox ()
driver.get("https://www.google.com")
time.sleep(3)
driver.quit()
