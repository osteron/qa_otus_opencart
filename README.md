# qa_otus_opencart
## Часть 2
- 1 Переписать уже имеющиеся тесты в проекта opencart на PageObject паттерн.
- 2 Добавить автотесты на следующие сценарии:
- 2.1 Добавление нового товара в разделе администратора
- 2.2 Удаление товара из списка в разделе администартора
- 2.3 Регистрация нового пользователя в магазине опенкарта - http://localhost:8081/index.php?route=account/register
- 2.4 Переключение валют из верхнего меню опенкарта - http://localhost:8081

## Запуск Opencart
> OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(hostname -I | grep -o "^[0-9.]*") docker-compose up -d