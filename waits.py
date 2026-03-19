from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()

'''Implicit wait 
 is applied globally and it will wait for the element to be present in the DOM
 for the specified time.
 
 If the element is found before the specified time, it will continue with the next step.
 If the element is not found within the specified time, it will throw a NoSuchElementException 
 
 Implicit wait is useful when you want to set a default waiting time for all elements in your test script.
 It is generally recommended to use implicit wait for elements that are expected to be present in the DOM
 but may take some time to load.
 '''
#driver.implicitly_wait(10)

'''Explicit wait
 is used to wait for a specific condition to occur before proceeding with the next step.
 It allows you to wait for a specific element to be present, visible, clickable, etc.
 Explicit wait is more flexible than implicit wait as it allows you to specify the condition you want to wait for.
 It is generally recommended to use explicit wait for elements that are expected to take some time to load
   or for elements that are not always present in the DOM.
 '''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver.get("https://demoqa.com/login")
driver.maximize_window()

wait = WebDriverWait(driver,10)

wait.until(EC.presence_of_element_located((By.ID, "userName"))).send_keys("vinayakkaralatti")
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Vinayak@123")
wait.until(EC.element_to_be_clickable((By.ID, "login"))).click()
print(driver.current_url)

driver.quit()

