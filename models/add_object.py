import uuid
import datetime
from connection import Connection

connection = Connection().connect


def add_object(name, stereotype, object_type, package_id, parent_id, ea_quid=""):
    with connection.cursor() as cursor:
        if (ea_quid == ''):
            ea_quid = '{' + str(uuid.uuid4()) + '}'
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype, package_id, parent_id, created_date))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Name`, `PDATA1` FROM `t_object` WHERE `ea_guid`=%s"
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()


#add_object("example", "example", "example", "1", "1")
