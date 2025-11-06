import allure
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.CalcPage import CalcPage


@allure.title("Тест калькулятора с задержкой")
@allure.description("Проверка работы калькулятора с установленной задержкой вычислений")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc():
    with allure.step("Инициализация драйвера и страницы калькулятора"):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        calc = CalcPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        calc.open()

    with allure.step(f"Установка времени задержки: 45 секунд"):
        time = "45"
        calc.delay_field(time)

    with allure.step("Выполнение вычисления: 7 + 8"):
        calc.calculation(7, "+", 8)

    with allure.step("Ожидание результата вычисления"):
        calc.wait_result()

    with allure.step("Получение результата с экрана"):
        res = calc.get_result()

    with allure.step("Проверка корректности результата"):
        assert res == "15", f"Ожидался результат 15, но получен {res}"
        allure.attach(f"Результат вычислений: {res}", name="Результат", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Закрытие браузера"):
        calc.close()

@allure.step("Проверка корректности результата вычислений")
def verify_calculation_result(actual_result: str, expected_result: str):
    """Вспомогательная функция для проверки результата"""
    assert actual_result == expected_result, f"Ожидался {expected_result}, но получен {actual_result}"
    allure.attach(f"✅ Результат корректен: {actual_result} = {expected_result}",
                  name="Проверка результата",
                  attachment_type=allure.attachment_type.TEXT)