import uuid
import datetime
import pymysql
def add_object(name, stereotype, object_type, package_id, parent_id, ea_quid=""):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        if (ea_quid == ''):
            ea_quid = '{' + str(uuid.uuid4()) + '}'
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype, parent_id, package_id, created_date)) #добавление объекта
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Name`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`  FROM `t_object` WHERE `ea_guid`=%s" #поиск объекта по ключу
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    return result
    connection.close()




def update_object(name, stereotype, object_id):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        modified_date = str(datetime.datetime.today())
        sql = "UPDATE `t_object` SET `Name`=%s, `Stereotype`=%s, `ModifiedDate`=%s WHERE `Object_ID`=%s" #поиск объекта по id и обновление нужных полей
        cursor.execute(sql, (name, stereotype, modified_date, object_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Stereotype`, `Name`, `PDATA1` FROM `t_object` WHERE `Object_ID`=%s"
        cursor.execute(sql, (object_id)) #проверка что данные изменились
        result = cursor.fetchone()
        print(result)
    return result
    connection.close()



