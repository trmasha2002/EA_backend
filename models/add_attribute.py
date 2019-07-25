import pymysql.cursors
import random
# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                             password='root',
                             db='easample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

def add_attribute(name, object_id):
    with connection.cursor() as cursor:
        ea_quid = str(random.randint(1, 100000))
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID` FROM `t_attribute` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()
add_attribute("first_attibute", "something", "attribute", "Component", "1")
