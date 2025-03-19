import time
import distutils.command.install
from tkinter import Radiobutton

from select import select
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_Obj = Service("C:/Users/vinuk/PycharmProjects/ChromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)

# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

#checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    checkbox.click()
    print(checkbox.get_attribute("value"))
    time.sleep(1)
    checkbox.click()

#Radio Buttons
Radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
Radiobutton[2].click()
time.sleep(2)

#hide and show
driver.find_element(By.ID, 'hide-textbox').click()
time.sleep(2)
if driver.find_element(By.ID, 'displayed-text').is_displayed():
    driver.find_element(By.ID, 'displayed-text').send_keys("it is hide and show")
else:
    driver.find_element(By.ID, 'show-textbox').click()
    time.sleep(1)
    driver.find_element(By.ID, 'displayed-text').send_keys("after, it is hide and show")
    time.sleep(1)

#alerts
name = "Vinayak"
driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.ID, 'alertbtn').click()
alrt = driver.switch_to.alert
print(alrt.text)
alrt.accept()