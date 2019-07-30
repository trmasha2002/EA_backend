import datetime

import pymysql.cursors
import random
import uuid
from connection import Connection
connection = Connection().connect
def add_diagram(name, package_id, stereotype, diagram_type):
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_diagram` (`Package_ID`, `Name`, `ea_guid`, `Stereotype`, `Diagram_Type`,`CreatedDate`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (package_id, name, ea_quid, stereotype, diagram_type, created_date))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Stereotype`, `Diagram_Type` FROM `t_diagram` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()
add_diagram("twelve", '6', 'package', 'pac')
