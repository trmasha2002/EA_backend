import uuid
import logging
from connection import connection
def add_connector(name, connector_type, start_objectid, end_objectid):
    """
    Создание конектора на основе полученных данных
    :param name: имя конектора
    :param connector_type: тип коннектора
    :param start_objectid: первый id объекта между которым идет связь
    :param end_objectid: второй id  объекта между которым идет связь
    :return: экземляр на основе полученных данных
    """
    logger = logging.getLogger("Connector")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        logger.info("Add Connector...")
        sql = "INSERT INTO `t_connector` (`Name`, `ea_guid`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID`) VALUES (?, ?, ?, ?, ?)" #добавление элемента
        cursor.execute(sql, (name, ea_quid, connector_type, start_objectid, end_objectid))
    connection.commit()
    result = get_by_ea_quid(ea_quid)
    return result

def get_by_ea_quid(ea_quid):
    """
    Получить экземпляр по ключу
    :param ea_quid: ключ
    :return: экземпляр на основе полученных данных
    """
    logger = logging.getLogger("Connector")
    logger.info("Get connector by ea_guid")
    with connection.cursor() as cursor:
        sql = "SELECT `Connector_ID`, `Name`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID` FROM `t_connector` WHERE `ea_guid`=?" #поиск по уникальному ключу
        result = cursor.execute(sql, (ea_quid)).fetchall()
    logger.info(result)
    return result

def update_by_ea_guid(ea_quid, name, connector_type, start_objectid, end_objectid):
    """
    Обновление по ключу
    :param ea_quid: уникальный ключ
    :param name: имя
    :param connector_type: тип конектора
    :param start_objectid: первый id
    :param end_objectid: второй id
    :return: измененного экземпляра на основе полученных данных
    """
    logger = logging.getLogger("Connector")
    logger.info("Update connector by ea_guid")
    with connection.cursor() as cursor:
        sql = "UPDATE `t_connector` SET `Name`=?, `Connector_Type`=?, `Start_Object_ID`=?, `End_Object_ID`=? WHERE ea_guid=?"
        cursor.execute(sql, (name, connector_type, start_objectid, end_objectid, ea_quid))
        connection.commit()
        result = get_by_ea_quid(ea_quid)
    return result

def delete_by_ea_guid(ea_guid):
    """
    Удаление экземпляра на основе ключа
    :param ea_guid: уникальный ключ
    :return: удаленного экземпляра
    """
    logger = logging.getLogger("Connector")
    logger.info("Delete connector by ea_guid")
    with connection.cursor() as cursor:
        sql = "DELETE FROM `t_connector` WHERE `ea_guid`=?"
        result = get_by_ea_quid(ea_guid)# поиск по уникальному ключу добавленного элемента
        cursor.execute(sql, (ea_guid))
    connection.commit()
    return result