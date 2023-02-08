# Домашнее задание к занятию "14.Средство визуализации Grafana"

## Обязательные задания

### Задание 1
Используя директорию [help](./help) внутри данного домашнего задания - запустите связку prometheus-grafana.

Зайдите в веб-интерфейс графана, используя авторизационные данные, указанные в манифесте docker-compose.

Подключите поднятый вами prometheus как источник данных.

Решение домашнего задания - скриншот веб-интерфейса grafana со списком подключенных Datasource.

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-03-grafana/Снимок%20экрана%202023-02-05%20в%2021.11.39.png)

## Задание 2
Изучите самостоятельно ресурсы:
- [promql-for-humans](https://timber.io/blog/promql-for-humans/#cpu-usage-by-instance)
- [understanding prometheus cpu metrics](https://www.robustperception.io/understanding-machine-cpu-usage)

Создайте Dashboard и в ней создайте следующие Panels:
- Утилизация CPU для nodeexporter (в процентах, 100-idle)
- CPULA 1/5/15
- Количество свободной оперативной памяти
- Количество места на файловой системе

Для решения данного ДЗ приведите promql запросы для выдачи этих метрик, а также скриншот получившейся Dashboard.

- 100 - (avg by (instance) (rate(node_cpu_seconds_total{job="nodeexporter",mode="idle"}[1m])) * 100)
- node_load1{instance="nodeexporter:9100"}, node_load5{instance="nodeexporter:9100"}, node_load15{instance="nodeexporter:9100"}
- node_memory_MemFree_bytes{instance="nodeexporter:9100"}/1024/1024
- node_filesystem_avail_bytes{instance="nodeexporter:9100",mountpoint="/",fstype!~"tmpfs|fuse.lxcfs"}/1024/1024/1024

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-03-grafana/Снимок%20экрана%202023-02-05%20в%2023.57.41.png)

## Задание 3
Создайте для каждой Dashboard подходящее правило alert (можно обратиться к первой лекции в блоке "Мониторинг").

Для решения ДЗ - приведите скриншот вашей итоговой Dashboard.

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-03-grafana/Снимок%20экрана%202023-02-08%20в%2012.08.31.png)

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-03-grafana/Снимок%20экрана%202023-02-08%20в%2012.16.21.png)

## Задание 4
Сохраните ваш Dashboard.

Для этого перейдите в настройки Dashboard, выберите в боковом меню "JSON MODEL".

Далее скопируйте отображаемое json-содержимое в отдельный файл и сохраните его.

В решении задания - приведите листинг этого файла.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
