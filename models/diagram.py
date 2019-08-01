import datetime
import uuid
import pymysql

def add_diagram(name, package_id, stereotype, diagram_type):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_diagram` (`Package_ID`, `Name`, `ea_guid`, `Stereotype`, `Diagram_Type`,`CreatedDate`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (package_id, name, ea_quid, stereotype, diagram_type, created_date))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Diagram_ID`, `Name`, `Package_ID`, `Stereotype`, `Diagram_Type` FROM `t_diagram` WHERE `ea_guid`=%s"
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()
    return result


