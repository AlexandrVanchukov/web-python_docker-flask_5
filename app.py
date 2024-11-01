import time
from flask import Flask, request
import psycopg2
from psycopg2 import sql
from datetime import datetime

app = Flask(__name__)

# Подключение к базе данных
def get_db_connection():
    connection = psycopg2.connect(
        host="db",
        database="counter_db",
        user="user",
        password="password"
    )
    return connection

# Функция для записи данных в базу
def log_request_info():
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = sql.SQL(
        "INSERT INTO counter (datetime, client_info) VALUES (%s, %s)"
    )
    current_time = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    client_info = request.headers.get('User-Agent')
    cursor.execute(insert_query, (current_time, client_info))
    connection.commit()
    cursor.close()
    connection.close()

# Функция для получения количества записей
def get_record_count():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM counter")
    count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return count

@app.route('/')
def hello():
    log_request_info()
    count = get_record_count()
    return f'Request logged successfully. Total records: {count}\n'
