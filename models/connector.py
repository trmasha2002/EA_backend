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
    logger = logging.getLogger("AddConnector")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        logger.info("Add Connector...")
        sql = "INSERT INTO `t_connector` (`Name`, `ea_guid`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID`) VALUES (?, ?, ?, ?, ?)" #добавление элемента
        cursor.execute(sql, (name, ea_quid, connector_type, start_objectid, end_objectid))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Connector_ID`, `Name`, `Connector_Type`, `Start_Object_ID`, `End_Object_ID` FROM `t_connector` WHERE `ea_guid`=?" #поиск по уникальному ключу
        result = cursor.execute(sql, (ea_quid)).fetchall()
        logger.info(result)
        print(result)
    connection.close()
    return result

