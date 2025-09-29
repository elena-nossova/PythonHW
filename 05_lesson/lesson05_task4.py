from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
sleep(5)

message = driver.find_element(By.CLASS_NAME, "flash.success").text
print("Сообщение:", message.replace("×", "").strip())

sleep(5)
driver.quit()