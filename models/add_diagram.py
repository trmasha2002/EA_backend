import pymysql.cursors
import random
import uuid
# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                             password='root',
                             db='easample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
def add_diagram(name, package_id, stereotype, diagram_type):
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        sql = "INSERT INTO `t_diagram` (`Package_ID`, `Name`, `ea_guid`, `Stereotype`, `Diagram_Type`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (package_id, name, ea_quid, stereotype, diagram_type))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Stereotype`, `Diagram_Type` FROM `t_diagram` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()
add_diagram("twelve", '6', 'package', 'pac')
