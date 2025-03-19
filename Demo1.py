import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service

# Service_Obj = Service("C:/Users/vinuk/PycharmProjects/SeleniumPython/ChromeDriver/chromedriver.exe")
# driver = webdriver.Chrome(service=Service_Obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


time.sleep(3)