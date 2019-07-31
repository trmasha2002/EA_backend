import pymysql.cursors
import random
from connection import Connection
import uuid
connection = Connection().connect


def add_attribute(name, object_id):
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID` FROM `t_attribute` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()


add_attribute("first_attibute", "something", "attribute", "Component", "1")
