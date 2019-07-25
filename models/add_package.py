import pymysql.cursors
import random
# Connect to the database
connection = pymysql.connect(host='localhost',
                            user='root',
                             password='root',
                             db='easample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

def add_package(name, notes, stereotype, object_type, parent_id):
    with connection.cursor() as cursor:
        ea_quid = str(random.randint(1, 100000))
        sql = "INSERT INTO `t_package` (`Name`, `Notes`, `ea_guid`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, notes, ea_quid))
        sql = "SELECT MAX(`Package_ID`) FROM `t_package`"
        cursor.execute(sql)
        result = cursor.fetchone()
        package_id = str(result['MAX(`Package_ID`)'])
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`, `Parent_ID`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype, package_id, parent_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Name` FROM `t_object` WHERE `Name`=%s"
        cursor.execute(sql, (name))
        result = cursor.fetchone()
        print(result)

    connection.close()

add_package('Package6','something11', 'stereotype12', 'Package', '1')