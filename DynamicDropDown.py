import time
import distutils.command.install

from select import select
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_Obj = Service("C:/Users/vinuk/PycharmProjects/ChromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)

# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
time.sleep(1)
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(1)

msg = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(msg)
assert msg == "India"