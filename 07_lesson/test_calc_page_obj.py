from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pages.CalcPage import CalcPage

def test_calc():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    calc = CalcPage(driver)
    calc.open()
    time = "45"
    calc.delay_field(time)
    calc.calculation(7, "+", 8)
    calc.wait_result()
    res = calc.get_result()

    assert res == "15"

    calc.close()
