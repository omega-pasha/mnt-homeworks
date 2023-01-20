# Домашнее задание к занятию "13.Системы мониторинга"

## Обязательные задания

1. Опишите основные плюсы и минусы pull и push систем мониторинга.
```
Pull - По сути это централизация сбора метрик. А это значит простота настройки и распределения общих метрик. 
Например CPU, память и т.д. Легче контролировать подлинность данных. Простота отладки и дебагинга, поскольку данные система получает по протоколу HTTP.

Из минусов - работа с динамически создаваемыми системами.

Push - Клиент может высылать метрики, одновременно, в несколько реплик системы мониторинга. Гибкая настройка отправки метрик. В лекции назывался плюс - работа по UDP. Но насколько я знаю, pull системы тоже могут работать по udp.

Из минусов - нет гарантий подлинности данных
```
2. Какие из ниже перечисленных систем относятся к push модели, а какие к pull? А может есть гибридные?
```
    - Prometheus - В основе своей это Pull модель. Но имеет компонент push gateway.
    - TICK - Push
    - Zabbix - Гибридная, агенты можно настроить как в активный, так и в пассивный режим работы
    - VictoriaMetrics - это быстрая, экономичная и масштабируемая база данных временных рядов. Его можно использовать в качестве долгосрочного удаленного хранилища для хранения метрик Prometheus, InfluxDB, OpenTSDB, Graphite
    - Nagios - Гибридная
```

3. Склонируйте себе [репозиторий](https://github.com/influxdata/sandbox/tree/master) и запустите TICK-стэк, 
используя технологии docker и docker-compose.

В виде решения на это упражнение приведите выводы команд с вашего компьютера (виртуальной машины):
```
    - curl http://localhost:8086/ping -v
    
*   Trying 127.0.0.1:8086...
* Connected to localhost (127.0.0.1) port 8086 (#0)
> GET /ping HTTP/1.1
> Host: localhost:8086
> User-Agent: curl/7.84.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< Content-Type: application/json
< Request-Id: 7c44f329-94e8-11ed-8064-0242ac120003
< X-Influxdb-Build: OSS
< X-Influxdb-Version: 1.8.10
< X-Request-Id: 7c44f329-94e8-11ed-8064-0242ac120003
< Date: Sun, 15 Jan 2023 15:22:55 GMT
<
* Connection #0 to host localhost left intact
```
```
    - curl http://localhost:8888
   <!DOCTYPE html><html><head><link rel="stylesheet" href="/index.c708214f.css"><meta http-equiv="Content-type" content="text/html; charset=utf-8"><title>Chronograf</title><link rel="icon shortcut" href="/favicon.70d63073.ico"></head><body> <div id="react-root" data-basepath=""></div> <script type="module" src="/index.e81b88ee.js"></script><script src="/index.a6955a67.js" nomodule="" defer></script> </body></html>%
```
```
    - curl http://localhost:9092/kapacitor/v1/ping -v
    
*   Trying 127.0.0.1:9092...
* Connected to localhost (127.0.0.1) port 9092 (#0)
> GET /kapacitor/v1/ping HTTP/1.1
> Host: localhost:9092
> User-Agent: curl/7.84.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 204 No Content
< Content-Type: application/json; charset=utf-8
< Request-Id: c6d69646-94e8-11ed-806b-0242ac120004
< X-Kapacitor-Version: 1.6.5
< Date: Sun, 15 Jan 2023 15:25:00 GMT
<
* Connection #0 to host localhost left intact
    
```  

А также скриншот веб-интерфейса ПО chronograf (`http://localhost:8888`). 

https://disk.yandex.ru/i/RrWKKT5fIzkRzg

4. Изучите список telegraf inputs.

Добавьте в конфигурацию telegraf плагин - disk:
```
[[inputs.disk]]
  ignore_fs = ["tmpfs", "devtmpfs", "devfs", "iso9660", "overlay", "aufs", "squashfs"]
```
Так же добавьте в конфигурацию telegraf плагин - mem:
`[[inputs.mem]]`

`Вставил эти параметры в конец файла /Users/pavelpomorcev/docker/sandbox/telegraf/telegraf.conf`

После настройки перезапустите telegraf.

Перейдите в веб-интерфейс Chronograf (http://localhost:8888) и откройте вкладку Data explorer.

Нажмите на кнопку Add a query

Изучите вывод интерфейса и выберите БД telegraf.autogen

В measurments выберите mem->host->telegraf_container_id , а в fields выберите used_percent. Внизу появится график утилизации оперативной памяти в контейнере telegraf.

Вверху вы можете увидеть запрос, аналогичный SQL-синтаксису. Поэкспериментируйте с запросом, попробуйте изменить группировку и интервал наблюдений.

Приведите скриншот с отображением метрик утилизации места на диске (disk->host->telegraf_container_id) из веб-интерфейса.

https://disk.yandex.ru/i/l12S6pXKRNSqjA

5. Изучите список [telegraf inputs](https://github.com/influxdata/telegraf/tree/master/plugins/inputs). 
Добавьте в конфигурацию telegraf следующий плагин - [docker](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/docker):
```
[[inputs.docker]]
  endpoint = "unix:///var/run/docker.sock"
```

Дополнительно вам может потребоваться донастройка контейнера telegraf в `docker-compose.yml` дополнительного volume и 
режима privileged:
```
  telegraf:
    image: telegraf:1.4.0
    privileged: true
    volumes:
      - ./etc/telegraf.conf:/etc/telegraf/telegraf.conf:Z
      - /var/run/docker.sock:/var/run/docker.sock:Z
    links:
      - influxdb
    ports:
      - "8092:8092/udp"
      - "8094:8094"
      - "8125:8125/udp"
```

`Не сработало, пока не сделал docker exec -u root -it 81f04446e873  /bin/sh -c "chmod 666 /var/run/docker.sock"`

После настройке перезапустите telegraf, обновите веб интерфейс и приведите скриншотом список `measurments` в 
веб-интерфейсе базы telegraf.autogen . Там должны появиться метрики, связанные с docker.

Факультативно можете изучить какие метрики собирает telegraf после выполнения данного задания.

https://disk.yandex.ru/i/UrR8yUcahipFLg

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

В веб-интерфейсе откройте вкладку `Dashboards`. Попробуйте создать свой dashboard с отображением:

    - утилизации ЦПУ
    - количества использованного RAM
    - утилизации пространства на дисках
    - количество поднятых контейнеров
    - аптайм
    - ...
    - фантазируйте)
    
 https://disk.yandex.ru/i/gyY7ECuDIme3UQ

