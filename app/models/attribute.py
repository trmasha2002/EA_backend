import uuid
import logging
from app.connection import connection
def add_attribute(name, object_id):
    """
    Cоздание аттрибута на основе полученых данных
    :param name: имя аттрибута
    :param object_id: id объекта к которому пишется аттрибут
    :return: экземляр на основе полученных данных
    """
    logger = logging.getLogger("Attribute")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'#генерация уникального ключа
        logger.info("Insert attribute...")
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (?, ?, ?)" #добавление в таблицу
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    result = get_by_ea_guid(ea_quid)
    return result
def update_attribute(name, id):
    """
    Обновление атрибута
    :param name: имя атрибута
    :param object_id: id объекта
    :return: обновленого атрибута на основе полученных данных
    """
    logger = logging.getLogger("Attribute")
    logger.info("Update attribute...")
    with connection.cursor() as cursor:
        sql = "UPDATE `t_attribute` SET `Name`=? WHERE `ID`=?"
        result = cursor.execute(sql, (name, id))
    result = get_by_id(id)
    connection.commit()
    return result

def get_by_ea_guid(ea_guid):
    """
    Получение по уникальному ключу
    :param ea_guid: уникальный ключ
    :return: экземпляра на основе ключа
    """
    logger = logging.getLogger("Attribute")
    logger.info("Get attribute by ea_guid")
    with connection.cursor() as cursor:
        sql = "SELECT  `ID`, `Object_ID`, `Name` FROM `t_attribute` WHERE `ea_guid`=?" #поиск по уникальному ключу добавленного элемента
        result = cursor.execute(sql, (ea_guid)).fetchall()
    logger.info(result)
    return result

def get_by_id(id):
    """
    Получение по id
    :param id: id
    :return: экземпляр на основе полученных данных
    """
    logger = logging.getLogger("Attribute")
    logger.info("Get attribute by id")
    with connection.cursor() as cursor:
        sql = "SELECT  `ID`, `Object_ID`, `Name` FROM `t_attribute` WHERE `ID`=?"  # поиск по уникальному ключу добавленного элемента
        result = cursor.execute(sql, (id)).fetchall()
    logger.info(result)
    return result

def delete_by_ea_guid(ea_guid):
    """
    Удаление по уникальному ключу
     :param ea_guid: уникальный ключ
     :return: удаленного экземпляра на основе уникального ключа
    """
    logger = logging.getLogger("Attribute")
    logger.info("Delete attribute by ea_guid")
    with connection.cursor() as cursor:
        sql = "DELETE FROM `t_attribute` WHERE `ea_guid`=?"
        result = get_by_ea_guid(ea_guid)# поиск по уникальному ключу добавленного элемента
        cursor.execute(sql, (ea_guid))
    return result
