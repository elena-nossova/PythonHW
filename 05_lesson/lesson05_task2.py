from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://uitestingplayground.com/dynamicid")
sleep(3)
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

button.click()
print("Клик выполнен! (без использования динамического ID)")

sleep(5)

# при троекратном запуске скрипта, кнопка нажимается.
# Уникальный локатор для кнопки - btn-primary.