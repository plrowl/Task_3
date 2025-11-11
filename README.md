UI автотесты Stellar Burgers

Автотесты для веб-приложения [Stellar Burgers]

Установка и запуск
pip install -r requirements.txt
pytest
Для запуска в Firefox:
pytest --browser=firefox
Для отчёта Allure:
allure serve allure_results

** Описание тестов**
* test\registration.py – проверка регистрации нового пользователя.
* test\login.py – проверка входа в аккаунт различными способами.
* test\logout.py – проверка выхода из личного кабинета.
* test\personal.py – проверка корректного отображения данных пользователя в личном кабинете.
* test\ingredient\tabs.py – проверка переключения вкладок ингредиентов на главной странице.