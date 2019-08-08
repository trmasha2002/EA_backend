import pymysql
import pyodbc
from models.connection import connection
def add_diagramobjects(diagram_id, object_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `t_diagramobjects` (`Object_ID`, `Diagram_ID`) VALUES (?, ?)"#добавление объекта
        cursor.execute(sql, (object_id, diagram_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT MAX(`Instance_ID`) FROM `t_diagramobjects`" #взятие последнего добавленого элемента
        result = cursor.execute(sql).fetchall()[0]
        instance_id = result
        sql = "SELECT `Instance_ID`, `Object_ID`, `Diagram_ID` FROM `t_diagramobjects` WHERE `Instance_ID`=?" #поиск последнего добавленого элемента
        result = cursor.execute(sql, (instance_id)).fetchall()
        print(result)
    connection.close()
    return result

