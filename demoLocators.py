import time

from select import select
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Service_Obj = Service("C:/Users/vinuk/PycharmProjects/ChromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service=Service_Obj)

# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)
#name using CSSselector -> tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Vinayak")
# time.sleep(2)
#email
driver.find_element(By.NAME, "email").send_keys("vinayak.karalatti@gmail.com")
# time.sleep(2)
#password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456789")
# time.sleep(2)
#checkbox
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(2)

#gender
gender = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))

gender.select_by_index(1)
time.sleep(2)
gender.select_by_visible_text("Male")
time.sleep(2)

#submit button using Xpath -> //tagname[@attribute='value']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
# time.sleep(2)

#message check by class name
msg = driver.find_element(By.CLASS_NAME,"alert-success").text
print(msg)
assert "Success! The Form has been submitted successfully!." in msg