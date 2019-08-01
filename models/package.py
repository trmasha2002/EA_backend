import datetime

import pymysql.cursors
import uuid
from models import object

def add_package(name, notes, stereotype, object_type, parent_id):
    connection = pymysql.connect(host='localhost',
                                 user='root',  #подключение к базе данных
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_package` (`Name`, `Notes`, `ea_guid`, `CreatedDate`) VALUES (%s, %s, %s, %s)" #добавление пакета
        cursor.execute(sql, (name, notes, ea_quid, created_date))
        sql = "SELECT MAX(`Package_ID`) FROM `t_package`"
        cursor.execute(sql)
        result = cursor.fetchone()
        package_id = str(result['MAX(`Package_ID`)']) #взятие id добавленого пакета
        object.add_object(name, stereotype, object_type, package_id, parent_id, ea_quid)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes`, `CreatedDate`  FROM `t_package` WHERE `ea_guid`=%s" #поиск добавленого пакета по ключу
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    return result
    connection.close()


def update_package(name, notes, stereotype, package_id):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        modified_data = str(datetime.datetime.today())
        sql = "UPDATE `t_package` SET `Name`=%s, `Notes`=%s WHERE `Package_ID`=%s"
        cursor.execute(sql, (name, notes, package_id)) #обновление пакета
        sql = "UPDATE `t_object` SET `Name`=%s, `Stereotype`=%s, `ModifiedDate`=%s, `Note`=%s WHERE `PDATA1`=%s"
        cursor.execute(sql, (name, stereotype, modified_data, notes, package_id)) # обновление объекта
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Name`, `Notes` FROM `t_package` WHERE `Package_ID`=%s"
        cursor.execute(sql, (package_id)) # проверка что данные объекта изменились
        result = cursor.fetchone()
        print(result)
        return result
    connection.close()
