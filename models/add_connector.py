import pymysql.cursors
import random
import uuid
from connection import Connection
connection = Connection().connect
def add_connector(name, connector_type, start_objectid, end_objectid):
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        sql = "INSERT INTO `t_connector` (`Name`, `ea_guid`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, ea_quid, connector_type, start_objectid, end_objectid))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Name`, `Connector_Type`, `Start_Object_ID` FROM `t_connector` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()

add_connector("example", "app-link", "12", "13")
