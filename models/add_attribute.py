import pymysql.cursors
import random
# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                             password='root',
                             db='easample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

def add_attribute(name, notes, stereotype, object_type):
    with connection.cursor() as cursor:
        ea_quid = str(random.randint(1, 100000))
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype))
        sql = "SELECT MAX(`Object_ID`) FROM `t_object`"
        cursor.execute(sql)
        result = cursor.fetchone()
        object_id = str(result['MAX(`Object_ID`)'])
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID` FROM `t_attribute` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()
add_attribute("first_attibute", "something", "attribute", "Component")
