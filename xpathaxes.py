from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. Open Chrome
driver = webdriver.Chrome ()
driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

#Self 
text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='India Cements Lt']/self::a").text
print(text_msg)



# 6. Close browser after 40 seconds
time.sleep(10)
driver.quit()