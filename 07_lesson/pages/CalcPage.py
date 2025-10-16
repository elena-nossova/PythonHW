from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay_field(self, time):
        delay_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_field.clear()
        delay_field.send_keys(time)

    # def click_button(self):
    #     self.driver.find_element(By.XPATH, "//span[text()='7']").click()
    #     self.driver.find_element(By.XPATH, "//span[text()='+']").click()
    #     self.driver.find_element(By.XPATH, "//span[text()='8']").click()
    #     self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def click_button(self, button_text):
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    def calculation(self, num1, operator, num2):
        self.click_button(str(num1))
        self.click_button(operator)
        self.click_button(str(num2))
        self.click_button("=")

    def wait_result(self):
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    def get_result(self):
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        return result

    def close(self):
        self.driver.quit()