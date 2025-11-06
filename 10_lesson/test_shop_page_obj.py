import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.ShopPage import ShopPage


@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description(
    "Полный процесс оформления заказа: авторизация, вход, добавление товаров, заполнение данных, проверка суммы")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop():
    with allure.step("Инициализация Firefox драйвера"):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        shop = ShopPage(driver)


        with allure.step("Открытие страницы магазина"):
            shop.open()

        with allure.step("Авторизация в системе"):
            shop.login()
            allure.attach("Успешная авторизация", name="Авторизация", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Добавление товаров в корзину"):
            shop.add_to_cart()
            allure.attach("Добавлены товары: рюкзак, футболка, комбинезон",
                          name="Товары в корзине",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Переход в корзину"):
            shop.go_to_cart()

        with allure.step("Начало оформления заказа"):
            shop.checkout()

        with allure.step("Заполнение информации о покупателе"):
            shop.fill_buyer_info("Elena", "Nosova", "141800")
            allure.attach("Данные покупателя: Elena Nosova, индекс 141800",
                          name="Информация о покупателе",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Продолжение процесса покупки"):
            shop.continue_to_buy()

        with allure.step("Получение итоговой суммы заказа"):
            total_amount = shop.get_total_amount()
            allure.attach(f"Итоговая сумма: ${total_amount}",
                          name="Сумма заказа",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Проверка корректности итоговой суммы"):
            verify_total_amount(total_amount, "58.29")

        with allure.step("Закрытие браузера"):
            shop.close()


@allure.step("Проверка итоговой суммы заказа")
def verify_total_amount(actual_amount: str, expected_amount: str):
    """Вспомогательная функция для проверки суммы заказа"""
    assert actual_amount == expected_amount, f"Ожидалась сумма ${expected_amount}, но получена ${actual_amount}"
    allure.attach(f"✅ Сумма заказа корректна: ${actual_amount}",
                  name="Проверка суммы",
                  attachment_type=allure.attachment_type.TEXT)