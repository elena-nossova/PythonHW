from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.ShopPage import ShopPage

def test_shop():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    shop = ShopPage(driver)

    shop.open()
    shop.login()
    shop.add_to_cart()
    shop.go_to_cart()
    shop.checkout()
    shop.fill_buyer_info()
    shop.continue_to_buy()

    total_amount = shop.get_total_amount()

    assert total_amount == "58.29", f"Ожидалось 58.29, но получили {total_amount}"
    print(f"✅ Тест пройден! Итоговая сумма: ${total_amount}")

    shop.close()
