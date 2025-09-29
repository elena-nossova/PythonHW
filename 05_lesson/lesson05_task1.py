from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")
sleep(2)

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
blue_button.click()

sleep(5)

# при каждом новом запросе скрипт работает по-разному: класс и положение кнопок меняется!
# уникальный локатор для голубой кнопки - btn-prymery