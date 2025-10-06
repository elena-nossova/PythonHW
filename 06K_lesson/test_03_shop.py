from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_shop():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Elena")
    driver.find_element(By.ID, "last-name").send_keys("Nosova")
    driver.find_element(By.ID, "postal-code").send_keys("141800")

    driver.find_element(By.ID, "continue").click()

    total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_amount = total_element.text.replace("Total: $", "")

    assert total_amount == "58.29"

    print(f"✅ Тест пройден! Итоговая сумма: ${total_amount}")

    driver.quit()
