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
    logger = logging.getLogger("Package")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        logger.info("Insert package...")
        sql = "INSERT INTO `t_package` (`Name`, `Notes`, `ea_guid`, `CreatedDate`, `ModifiedDate`) VALUES (?, ?, ?, ?, ?)" #добавление пакета
        cursor.execute(sql, (name, notes, ea_quid, created_date, created_date))
        sql = "SELECT `Package_ID` FROM `t_package` WHERE `ea_guid`=?"
        result = cursor.execute(sql, (ea_quid)).fetchall()
    package_id = str(result[0][0])
    result = get_by_ea_guid(ea_quid)
    print(result)
    object.add_object(name, stereotype, object_type, package_id, parent_id, ea_quid)
    logger.info(result)
    result = object.get_by_ea_guid(ea_quid)
    return result

def get_by_ea_guid(ea_guid):
    """
    Получение по ключу
    :param ea_guid: уникальный ключ
    :return: экземпляра
    """
    logger = logging.getLogger("Package")
    logger.info("Get package by ea_guid")
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes`, `CreatedDate`, `ModifiedDate`  FROM `t_package` WHERE `ea_guid`=?" #поиск добавленого пакета по ключу
        result = cursor.execute(sql, ea_guid).fetchall()
    logger.info(result)
    return result

def get_by_id(package_id):
    """
    Получение по id
    :param package_id: id
    :return: экземпляра
    """
    logger = logging.getLogger("Package")
    logger.info("Get package by id")
    with connection.cursor() as cursor:
        sql = "SELECT `Package_ID`, `Name`, `Notes` FROM `t_package` WHERE `Package_ID`=?"
        result = cursor.execute(sql, (package_id)).fetchall()  # проверка что данные объекта изменились
    logger.info(result)
    return result
def update_package(name, notes, stereotype, package_id):
    """
    Измененин данных пакета на основе полученных данных
    :param name: имя пакета
    :param notes: описание пакета
    :param stereotype: стереоптип
    :param package_id: id пакета
    :return: экземпляр пакета на основе изменненых данных
    """
    logger = logging.getLogger("Package")
    with connection.cursor() as cursor:
        modified_data = str(datetime.datetime.today())
        logger.info("Update package...")
        sql = "UPDATE `t_package` SET `Name`=?, `Notes`=? WHERE `Package_ID`=?"
        cursor.execute(sql, (package_id, name, notes))
    connection.commit()
    sql = "SELECT `Object_ID` FROM `t_object` WHERE `PDATA1`=?"
    result = cursor.execute(sql, (package_id)).fetchall()
    object_id = result[0][0]
    object.update_object(name, stereotype, object_id)
    return result

def delete_by_ea_guid(ea_guid):
    """
    Удаление по уникальному ключу
    :param ea_guid: ключ
    :return: возращение удаленного объекта
    """
    logger = logging.getLogger("Package")
    logger.info("Delete package by ea_guid")
    with connection.cursor() as cursor:
        sql = "DELETE FROM `t_package` WHERE `ea_guid`=?"
        result = get_by_ea_guid(ea_guid)# поиск по уникальному ключу добавленного элемента
        cursor.execute(sql, (ea_guid))
    connection.commit()
    object.delete_by_ea_guid(ea_guid)
    return result