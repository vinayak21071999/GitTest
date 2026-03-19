from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


browserName = "Chrome"

if browserName == "Chrome":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "Safari":
    driver = webdriver.Safari()
else:
    print("provide correct browser")
    #raise Exception("broswer name is wrong")
    raise SystemExit

driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, "username").send_keys("vinayakkaralatti@gmial.com")
#driver.find_element(By.ID, "email-submit-button").click()
time.sleep(5)

print(driver.current_url)

driver.quit()

