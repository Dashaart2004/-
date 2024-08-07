# YouGile

## Описание

Проект автоматизации тестирования сервиса YouGile - инструмент для управления проектами и задачами
Данный проект является продолжением работы по ручному тестированию сервиса, который доступен по  ссылке https://ru.yougile.com/team/settings-account 


## Введение

Работа состоит из двух частей: UI и API-тесты, по пять автотестов в обоих случаях. 
Тест-план https://gabby-windscreen-dca.notion.site/YouGile-e3ac866895754f37883adca4af415ba9
Язык программирования- Python


## Стек и библиотеки:

pytest -- pip install pytest
selenium -- pip install selenium
allure -- pip install allure-pytest
pip install webdriver-manager


## Шаги:

- 1.Склонировать проект (git clone)
- 2.Установить все зависимости 'pip3 freeze > requirements.txt'
- 3.Запустить все тесты 'pytets'
- 4.Сгенерировать отчет 'allure generate allure-files -o allure-report'
- 5.Открыть отчет 'allure open allure-report'
- 6.Чтобы запустить только ui-тесты ввести 'pytest -m ui_test'
- 7.Чтобы запустить только API-тесты ввести 'pytest -m api_test'
