1. Запихнуть проект в контернер, чтобы размер был минимальным. Добавить какую-нибудь новую вьюху, собрать новый имадж, 
сравнить, какие слои были затронуты.
2. Сделать docker-compose. Нужен сервис, редис, постгрес. Нужно сделать так, чтобы торчал наружу только один порт.
Должны торчать ручки:
```http request
GET http://localhost:8080/
```
```http request
GET http://localhost:8080/some/
```
```http request
GET http://localhost:8080/healthcheck/
```
3. Написать докерфайл и докер-композ для локальной разработки. Здесб будет важным фактом то, чтобы не надо было
собирать контейнер каждый раз при изменении кода