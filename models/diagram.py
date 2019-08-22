import datetime
import uuid
from connection import connection
import logging
def add_diagram(name, package_id, stereotype, diagram_type):
    """
    Создание диаграммы на основе полученных данных
    :param name: имя диаграммы
    :param package_id: id пакета внутри которого находится диаграмма
    :param stereotype: стереотип
    :param diagram_type: тип диаграммы
    :return: экземпляр на основе полученных данных
    """
    logger = logging.getLogger("Diagram")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        logger.info("Add Diagram...")
        sql = "INSERT INTO `t_diagram` (`Package_ID`, `Name`, `ea_guid`, `Stereotype`, `Diagram_Type`,`CreatedDate`) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (package_id, name, ea_quid, stereotype, diagram_type, created_date)) #добавление элемента
    connection.commit()
    result = get_by_ea_guid(ea_quid)
    return result

def get_by_ea_guid(ea_quid):
    """
    Получение экземпляра по ключу
    :param ea_quid: уникальный ключ
    :return:
    """
    logger = logging.getLogger("Diagram")
    logger.info("Get diagram by ea_guid")
    with connection.cursor() as cursor:
        sql = "SELECT `Diagram_ID`, `Name`, `Package_ID`, `Stereotype`, `Diagram_Type` FROM `t_diagram` WHERE `ea_guid`=?" #поиск по уникальному ключу
        result = cursor.execute(sql, (ea_quid)).fetchall()
    logger.info(result)
    return result

def delete_by_ea_guid(ea_guid):
    """
    Удаление по ключу
    :param ea_guid: уникальный
    :return:
    """
    logger = logging.getLogger("Diagram")
    logger.info("Delete diagram by ea_guid")
    with connection.cursor() as cursor:
        sql = "DELETE FROM `t_diagram` WHERE `ea_guid`=?"
        result = get_by_ea_guid(ea_guid)# поиск по уникальному ключу добавленного элемента
        cursor.execute(sql, (ea_guid))
    connection.commit()
    return result

def update_by_ea_guid(name, stereotype, diagram_type, ea_guid):
    """
    Обновление диаграммы на основе полученнных данных
    :param name: имя
    :param stereotype: стереотип
    :param diagram_type: тип диаграммы
    :param ea_guid: уникальный ключ
    :return: обновленного элемента на основе полученных данных
    """
    logger = logging.getLogger("Diagram")
    logger.info("Update diagram by ea_guid")
    with connection.cursor() as cursor:
        sql = "UPDATE `t_diagram` SET `Name`=?, `Stereotype`=?, `Diagram_Type`=? WHERE ea_guid=?"
        cursor.execute(sql, (name, stereotype, diagram_type, ea_guid))
        connection.commit()
        result = get_by_ea_guid(ea_guid)
    return result