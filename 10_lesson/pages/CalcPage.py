from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union


class CalcPage:
    """Класс для работы со страницей калькулятора"""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы калькулятора"""
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открытие страницы калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay_field(self, time: Union[str, int]) -> None:
        """Установка времени задержки вычисления"""
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(str(time))

    def click_button(self, button_text: str) -> None:
        """Нажатие кнопки калькулятора"""
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    def calculation(self, num1: Union[str, int], operator: str, num2: Union[str, int]) -> None:
        """Выполнение вычисления"""
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button("=")

    def wait_result(self, expected_result: str = "15") -> None:
        """Ожидание появления результата на экране"""
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_result))

    def get_result(self) -> str:
        """Получение результата с экрана калькулятора"""
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result

    def close(self) -> None:
        """Закрытие браузера"""
        self.driver.quit()
