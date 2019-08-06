import pymysql.cursors
import uuid
import pyodbc
from models import connection
connection = connection.connection
def add_attribute(name, object_id):
    #connection = pyodbc.connect("Driver={Devart ODBC Driver for MySQL};"
    #                        "Server=localhost;"
    #                      "Database=easample;"
    #                        "USER=root;"
    #                        "PASSWORD=root;"
    #                        "OPTION=3;")


    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'#генерация уникального ключа
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (?, ?, ?)" #добавление в таблицу
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT  `ID`, `Object_ID`, `Name` FROM `t_attribute` WHERE `ea_guid`=?" #поиск по уникальному ключу добавленного элемента
        result = cursor.execute(sql, (ea_quid)).fetchall()
        print(result)
    connection.close()
    return result

