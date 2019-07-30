import datetime

import pymysql.cursors
import random
import uuid
from connection import Connection
from add_object import add_object
connection = Connection().connect


def add_package(name, notes, stereotype, object_type, parent_id):
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_package` (`Name`, `Notes`, `ea_guid`, `CreatedDate`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, notes, ea_quid, created_date))
        sql = "SELECT MAX(`Package_ID`) FROM `t_package`"
        cursor.execute(sql)
        result = cursor.fetchone()
        package_id = str(result['MAX(`Package_ID`)'])
        #ea_quid = '{' + str(uuid.uuid4()) + '}'
        #sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        #cursor.execute(sql, (object_type, name, ea_quid, stereotype, package_id, parent_id, created_date))
        add_object(name, stereotype, object_type, package_id, parent_id, ea_quid)
    connection.commit()
    print("hello")
    with connection.cursor() as cursor:
        sql = "SELECT `ea_guid`, `Name` FROM `t_object` WHERE `ea_guid`=%s"
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()


add_package('Package6', 'something11', 'stereotype12', 'Package', '1')
