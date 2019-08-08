import uuid
import datetime
from connection import connection
def add_object(name, stereotype, object_type, package_id, parent_id, ea_quid=""):
    with connection.cursor() as cursor:
        if (ea_quid == ''):
            ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype, parent_id, package_id, created_date)) #добавление объекта
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Name`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`  FROM `t_object` WHERE `ea_guid`=?" #поиск объекта по ключу
        result = cursor.execute(sql, (ea_quid)).fetchall()
        print(result)
    return result
    connection.close()




def update_object(name, stereotype, object_id):

    with connection.cursor() as cursor:
        modified_date = str(datetime.datetime.today())
        sql = "UPDATE `t_object` SET `Name`=?, `Stereotype`=?, `ModifiedDate`=? WHERE `Object_ID`=?" #поиск объекта по id и обновление нужных полей
        cursor.execute(sql, (name, stereotype, modified_date, object_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Stereotype`, `Name`, `PDATA1` FROM `t_object` WHERE `Object_ID`=?"
        result = cursor.execute(sql, (object_id)).fetchall()#проверка что данные изменились
        print(result)
    return result
    connection.close()


