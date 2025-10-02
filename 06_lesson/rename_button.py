from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/textinput")

search_field = "#newButtonName"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()

button_text = button.text
print(button_text)

driver.quit()

#newButtonName - поле My button
#updatingButton - синяя кнопка