from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
)

waiter = WebDriverWait(driver, 40, 0.1)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

img_third = waiter.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award"))
)

img_src = img_third.get_attribute("src")
print(img_src)

driver.quit()
