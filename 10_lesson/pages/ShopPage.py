from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class ShopPage:
    """Класс для работы со страницей интернет-магазина"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы магазина"""
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """Открытие страницы магазина"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str = "standard_user", password: str = "secret_sauce") -> None:
        """Выполнение входа в систему"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_to_cart(self) -> None:
        """Добавление товаров в корзину"""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """Переход в корзину"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self) -> None:
        """Начало процесса оформления заказа"""
        self.driver.find_element(By.ID, "checkout").click()

    def fill_buyer_info(self, first_name: str = "Elena", last_name: str = "Nosova",
                        postal_code: str = "141800") -> None:
        """Заполнение информации о покупателе"""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_to_buy(self) -> None:
        """Продолжение процесса покупки после заполнения информации"""
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self) -> str:
        """Получение итоговой суммы заказа"""
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_amount = total_element.text.replace("Total: $", "")
        return total_amount

    def close(self) -> None:
        """Закрытие браузера"""
        self.driver.quit()