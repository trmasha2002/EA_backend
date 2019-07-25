import pymysql.cursors
import random
# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                             password='root',
                             db='easample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)




def add_object(name, stereotype, object_type, package_id):
    with connection.cursor() as cursor:
        ea_quid = str(random.randint(1, 100000))
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype, package_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Name` FROM `t_object` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)
    connection.close()

add_object("example", "example", "example", "1")

