# Selenium Test
from selenium import webdriver

driver = webdriver.Chrome()
print("start driver")
driver.get("http://selenium.dev")
print("get driver")
driver.quit()
print("quit driver")