from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://demoqa.com/login")
driver.maximize_window()
driver.find_element(By.ID, "userName").send_keys("vinayakkaralatti")
driver.find_element(By.ID, "password").send_keys("Vinayak@123")
driver.find_element(By.ID, "login").click()
print(driver.current_url)
time.sleep(5)
driver.quit()