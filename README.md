# PythonHW
markdown
# Проект автоматизации тестирования с Allure отчетами

Проект содержит автоматизированные тесты для веб-приложений с использованием Selenium WebDriver и генерацией отчетов в Allure.

## 🚀 Технологии

- **Python** - язык программирования
- **Selenium WebDriver** - автоматизация браузера
- **Pytest** - фреймворк для тестирования
- **Allure** - система отчетности
- **WebDriver Manager** - автоматическое управление драйверами

## 📁 Структура проекта
Project/PythonHW

Directory/ 10_lesson

pages/Page Object классы:

--CalcPage.py # Страница калькулятора

-- ShopPage.py # Страница интернет-магазина

Тестовые файлы

-- test_calc_page_obj.py

-- test_shop_page_obj.py

requirements.txt # Зависимости проекта

README.md # Документация



## ⚙️ Установка зависимостей

# Установка необходимых пакетов
pip install -r requirements.txt

# Или установка вручную
pip install selenium pytest allure-pytest webdriver-manager

# Запуск тестов в Firefox (рекомендуется)
# Запуск теста магазина
python -m pytest test_shop_page_obj.py --alluredir allure-results

# Запуск теста калькулятора  
python -m pytest test_calc_page_obj.py --alluredir allure-results
# В файле теста замените Firefox на Chrome
# Установка Chrome WebDriver
pip install webdriver-manager

# Важные замечания:
Firefox рекомендуется для стабильной работы с демо-сайтами

Chrome может показывать предупреждения о безопасност

# Просмотр отчета
allure serve allure-results
Запуск в Chrome (если требуется)

Allure отчеты генерируются в папку allure-results
🧪 Запуск тестов
Запуск всех тестов

python -m pytest --alluredir=allure-results

Запуск конкретного тестового файла

# Запуск тестов калькулятора
python -m pytest tests/test_calc_page_obj.py --alluredir=allure-results

# Запуск тестов магазина
python -m pytest tests/test_shop_page_obj.py --alluredir=allure-results

# Запуск с подробным выводом
python -m pytest -v --alluredir=allure-results

📊 Просмотр отчетов Allure
Генерация и открытие отчета

# Запуск локального сервера с отчетом
allure serve allure-results
Генерация статического отчета

# Генерация HTML отчета в папку
allure generate allure-results -o allure-report --clean

# Открытие сгенерированного отчета
allure open allure-report
📝 Описание тестов
🧮 Тесты калькулятора (test_calc_page_obj.py)
Тест: Проверка работы калькулятора с задержкой

Сценарий: Установка задержки, выполнение операции 7+8, проверка результата

Ожидаемый результат: 15

🛍️ Тесты интернет-магазина (test_shop_page_obj.py)
Тест: Оформление заказа в интернет-магазине

Сценарий: Авторизация, добавление товаров в корзину, оформление заказа

Ожидаемый результат: Итоговая сумма $58.29

🔧 Настройка окружения
Установка Allure на Windows
bash
# Установка через Scoop
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install allure

📈 Генерация различных отчетов
Отчет для конкретного теста
bash
python -m pytest tests/test_calc_page_obj.py::test_calc --alluredir=allure-calc
allure serve allure-calc
Сравнение нескольких запусков
bash
# Первый запуск
python -m pytest --alluredir=allure-run-1

# Второй запуск  
python -m pytest --alluredir=allure-run-2
🚫 Исключения из репозитория
В файле .gitignore добавлены:

allure-results/    # временные данные для генерации отчетов
allure-report/     # сгенерированные HTML отчеты
*.pyc             # скомпилированные файлы Python
__pycache__/      # кеш Python

📞 Поддержка
При возникновении вопросов по запуску тестов или генерации отчетов обращайтесь к документации:

Allure Framework

Pytest Documentation

Selenium Python

## 📁 **Также создан файл `requirements.txt`:**
selenium==4.15.0
pytest==7.4.0
allure-pytest==2.13.0
webdriver-manager==4.0.0
