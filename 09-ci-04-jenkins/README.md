# Домашнее задание к занятию "10.Jenkins"
## Подготовка к выполнению

1. Создать 2 VM: для jenkins-master и jenkins-agent.

Создал 2 виртуальные машины - https://disk.yandex.ru/i/0FAIdoYTJXl1uQ

2. Установить jenkins при помощи playbook'a.
3. Запустить и проверить работоспособность.

Проверил сделав простой билд, который просто выведет содержимое директории - https://disk.yandex.ru/i/d38cQrXDGSNK3A

4. Сделать первоначальную настройку.

Настроил подключение агента - https://disk.yandex.ru/i/09C5nFhqU3HY_w

## Основная часть
1. Сделать Freestyle Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.

- Настроил хранение только 5 билдов - https://disk.yandex.ru/i/XaAkDssnzXSS2g
- Подключился к репозиторию - https://disk.yandex.ru/i/iY762ojLZBDfqA
- Настроил несколько шагов сборки - https://disk.yandex.ru/i/xBtAMd_iKjroDw
- Запустил билд, он склонировал репозиторий по заданным Credentials, вывел содержимое папки и запустил `molecule test` - https://disk.yandex.ru/i/ozH_4gvNhg0tUw

2. Сделать Declarative Pipeline Job, который будет запускать `molecule test` из любого вашего репозитория с ролью.
3. Перенести Declarative Pipeline в репозиторий в файл `Jenkinsfile`.
4. Создать Multibranch Pipeline на запуск `Jenkinsfile` из репозитория.
5. Создать Scripted Pipeline, наполнить его скриптом из [pipeline](./pipeline).
6. Внести необходимые изменения, чтобы Pipeline запускал `ansible-playbook` без флагов `--check --diff`, если не установлен параметр при запуске джобы (prod_run = True), по умолчанию параметр имеет значение False и запускает прогон с флагами `--check --diff`.
7. Проверить работоспособность, исправить ошибки, исправленный Pipeline вложить в репозиторий в файл `ScriptedJenkinsfile`.
8. Отправить ссылку на репозиторий с ролью и Declarative Pipeline и Scripted Pipeline.

