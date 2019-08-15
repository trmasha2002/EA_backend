import datetime
import logging
import uuid
from models import object
from connection import connection
def add_package(name, notes, stereotype, object_type, parent_id):
    logger = logging.getLogger("AddPackage")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        logger.info("Insert package...")
        sql = "INSERT INTO `t_package` (`Name`, `Notes`, `ea_guid`, `CreatedDate`) VALUES (?, ?, ?, ?)" #добавление пакета
        cursor.execute(sql, (name, notes, ea_quid, created_date))
        sql = "SELECT `Package_ID` FROM `t_package` WHERE `ea_guid`=?"
        result = cursor.execute(sql, (ea_quid)).fetchall()
        package_id = str(result[0])
        object.add_object(name, stereotype, object_type, package_id, parent_id, ea_quid)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes`, `CreatedDate`  FROM `t_package` WHERE `ea_guid`=?" #поиск добавленого пакета по ключу
        result = cursor.execute(sql, ea_quid).fetchall()
        print(result)
        logger.info(result)
    return result
    connection.close()


def update_package(name, notes, stereotype, package_id):
    logger = logging.getLogger("UpdatePackage")
    with connection.cursor() as cursor:
        modified_data = str(datetime.datetime.today())
        logger.info("Update package...")
        sql = "SELECT `Package_ID` FROM `t_package`"
        result = cursor.execute(sql, ()).fetchall()
        good = False
        for x in result:
            if (x[0] == package_id):
                good = True
        if (not good):
            logger.error("Don't exist such package_id")
        sql = "UPDATE `t_package` SET `Name`=?, `Notes`=? WHERE `Package_ID`=?"
        cursor.execute(sql, (package_id, name, notes))
        sql = "UPDATE `t_object` SET `Name`=?, `Stereotype`=?, `ModifiedDate`=?, `Note`=? WHERE `PDATA1`=?"
        cursor.execute(sql, (name, stereotype, modified_data, notes, package_id)) # обновление объекта
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes` FROM `t_package` WHERE `Package_ID`=?"
        result =cursor.execute(sql, (package_id)).fetchall()# проверка что данные объекта изменились
        print(result)
        logger.info(result)
    return result
    connection.close()