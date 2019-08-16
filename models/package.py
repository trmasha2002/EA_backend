import datetime
import logging
import uuid
from models import object
from connection import connection
def add_package(name, notes, stereotype, object_type, parent_id):
    """
    Создание пакета
    :param name: имя пакета
    :param notes: описание пакета
    :param stereotype: стереотип
    :param object_type: тип объекта
    :param parent_id: id родителя пакета
    :return: экземпляр на основе полученных данных
    """
    logger = logging.getLogger("AddPackage")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        logger.info("Insert package...")
        sql = "INSERT INTO `t_package` (`Name`, `Notes`, `ea_guid`, `CreatedDate`, `ModifiedDate`) VALUES (?, ?, ?, ?, ?)" #добавление пакета
        cursor.execute(sql, (name, notes, ea_quid, created_date, created_date))
        sql = "SELECT `Package_ID` FROM `t_package` WHERE `ea_guid`=?"
        result = cursor.execute(sql, (ea_quid)).fetchall()
        package_id = str(result[0])
        object.add_object(name, stereotype, object_type, package_id, parent_id, ea_quid)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes`, `CreatedDate`, `ModifiedDate`  FROM `t_package` WHERE `ea_guid`=?" #поиск добавленого пакета по ключу
        result = cursor.execute(sql, ea_quid).fetchall()
        print(result)
        logger.info(result)
    return result
    connection.close()


def update_package(name, notes, stereotype, package_id):
    """
    Измененин данных пакета на основе полученных данных
    :param name: имя пакета
    :param notes: описание пакета
    :param stereotype: стереоптип
    :param package_id: id пакета
    :return: экземпляр пакета на основе изменненых данных
    """
    logger = logging.getLogger("UpdatePackage")
    with connection.cursor() as cursor:
        modified_data = str(datetime.datetime.today())
        logger.info("Update package...")
        sql = "UPDATE `t_package` SET `Name`=?, `Notes`=? WHERE `Package_ID`=?"
        cursor.execute(sql, (package_id, name, notes))
        sql = "SELECT `Object_ID` FROM `t_object` WHERE `PDATA1`=?"
        result = cursor.execute(sql, (package_id)).fetchall()
        object_id = result[0][0]
        object.update_object(name, stereotype, object_id)
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes` FROM `t_package` WHERE `Package_ID`=?"
        result = cursor.execute(sql, (package_id)).fetchall()# проверка что данные объекта изменились
        print(result)
        logger.info(result)
    return result
    connection.close()