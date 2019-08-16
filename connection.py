import pymysql.cursors
import pyodbc
import json

with open("connect.json", "r") as read_file:
    data = json.load(read_file)
"""
Настройки соединения
Driver: имя драйвера
Sever: адрес хоста
Database: имя базы данных
USER: имя пользователя
PASSWORD: пароль пользователя
OPTION: 
"""
str_connect = 'Driver={};Server={};Database={};USER={};PASSWORD={};OPTION={};'.format(data['Driver'],data['Server'], data['Database'], data['User'], data['Password'], data['Option'])
connection = pyodbc.connect(str_connect)
