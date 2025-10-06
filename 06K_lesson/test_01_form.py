from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


def test_form():
    service = EdgeService(r"C:\Users\admin\Desktop\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_contains("submitted"))

    zip_code_alert = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_alert.get_attribute("class")

    green_fields = [
        "first-name", "last-name", "address",
        "city", "country", "e-mail",
        "phone", "job-position", "company"
    ]

    for field_id in green_fields:
        field_alert = driver.find_element(By.ID, field_id)
        assert "alert-success" in field_alert.get_attribute("class")

    driver.quit()
