## Задание 1

Вам необходимо поднять в докере:
- elasticsearch(hot и warm ноды)
- logstash
- kibana
- filebeat

и связать их между собой.

Logstash следует сконфигурировать для приёма по tcp json сообщений.

Filebeat следует сконфигурировать для отправки логов docker вашей системы в logstash.

В директории [help](./help) находится манифест docker-compose и конфигурации filebeat/logstash для быстрого 
выполнения данного задания.

Результатом выполнения данного задания должны быть:
- скриншот `docker ps` через 5 минут после старта всех контейнеров (их должно быть 5)
- скриншот интерфейса kibana
- docker-compose манифест (если вы не использовали директорию help)
- ваши yml конфигурации для стека (если вы не использовали директорию help)

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-04-elk/Снимок%20экрана%202023-02-15%20в%2022.10.07.png)

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-04-elk/Снимок%20экрана%202023-02-15%20в%2022.58.38.png)

Использовал директорию help, только исправил пару параметров:
- не правильно указан путь
```
logstash:
    volumes:
      - ./configs/logstash.conf:/usr/share/logstash/pipeline/logstash.conf:Z
```
- не была указана общая сеть
```
filebeat:
    networks:
      - elastic
```
- прописал наименование индекса в logstash.conf
```
index => "logstash-%{+YYYY.MM.dd}"
```

## Задание 2

Перейдите в меню [создания index-patterns  в kibana](http://localhost:5601/app/management/kibana/indexPatterns/create)
и создайте несколько index-patterns из имеющихся.

Перейдите в меню просмотра логов в kibana (Discover) и самостоятельно изучите как отображаются логи и как производить 
поиск по логам.

В манифесте директории help также приведенно dummy приложение, которое генерирует рандомные события в stdout контейнера.
Данные логи должны порождать индекс logstash-* в elasticsearch. Если данного индекса нет - воспользуйтесь советами 
и источниками из раздела "Дополнительные ссылки" данного ДЗ.
 
![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-04-elk/Снимок%20экрана%202023-02-15%20в%2022.03.59.png)

![](https://github.com/omega-pasha/mnt-homeworks/blob/MNT-video/10-monitoring-04-elk/Снимок%20экрана%202023-02-15%20в%2022.22.06.png)

 
