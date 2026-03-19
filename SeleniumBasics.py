import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://google.com")
print(driver.title)

driver.find_element(By.NAME, "q").send_keys("selenium")
time.sleep(2)
optionsList = driver.find_elements(By.CSS_SELECTOR,"ul.G43f7e li span")
print(len(optionsList))

for element in optionsList:
    print(element.text)
    if element.text == "selenium python":
        element.click()
        time.sleep(5)
        break

driver.quit()