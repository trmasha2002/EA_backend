import datetime

import pymysql.cursors
import random
import uuid
from connection import Connection
from object import add_object
from object import update_object
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
        add_object(name, stereotype, object_type, package_id, parent_id, ea_quid)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `ea_guid`, `Name` FROM `t_object` WHERE `ea_guid`=%s"
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()


#add_package('Package6', 'something11', 'stereotype12', 'Package', '1')


def update_package(name, notes, stereotype, package_id):
    with connection.cursor() as cursor:
        modified_data = str(datetime.datetime.today())
        sql = "UPDATE `t_package` SET `Name`=%s, `Notes`=%s WHERE `Package_ID`=%s"
        cursor.execute(sql, (name, notes, package_id))
        sql = "UPDATE `t_object` SET `Name`=%s, `Stereotype`=%s, `ModifiedDate`=%s, `Note`=%s WHERE `PDATA1`=%s"
        cursor.execute(sql, (name, stereotype, modified_data, notes, package_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Name`, `Notes` FROM `t_package` WHERE `Package_ID`=%s"
        cursor.execute(sql, (package_id))
        result = cursor.fetchone()
        print(result)
    connection.close()

update_package("NewPackage", None, "executable", "2")
