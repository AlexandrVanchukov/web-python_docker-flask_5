Чтобы запустить проект нужно выполнить следующие команды в терминале:

1. Собрать образы контейнеров:
```bash
docker-compose up --build
```
2. Подключитесь к базе данных в контейнере:
```bash
docker exec -it web-python_docker-flask_5-db-1 psql -U user -d counter_db
```
3. Создайте таблицу:
```sql
CREATE TABLE counter (
    id SERIAL PRIMARY KEY,
    datetime VARCHAR(255),
    client_info TEXT
);
```
