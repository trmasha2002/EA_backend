import pymysql.cursors
import uuid


def add_attribute(name, object_id):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT  `ID`, `Object_ID`, `Name` FROM `t_attribute` WHERE `ea_guid`=%s"
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()
    return result

