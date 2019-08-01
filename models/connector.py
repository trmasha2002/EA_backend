import pymysql.cursors
import random
import uuid




def add_connector(name, connector_type, start_objectid, end_objectid):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        sql = "INSERT INTO `t_connector` (`Name`, `ea_guid`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (name, ea_quid, connector_type, start_objectid, end_objectid))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Connector_ID`, `Name`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID` FROM `t_connector` WHERE `ea_guid`=%s"
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()
    return result
