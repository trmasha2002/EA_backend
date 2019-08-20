import uuid
import datetime
import logging
from connection import connection
def add_object(name, stereotype, object_type, package_id, parent_id, ea_quid=""):
    """
    Создание объекта на основе полученных данных
    :param name: имя объекта
    :param stereotype: стереотип объекта
    :param object_type: тип объекта
    :param package_id: id добавленого пакета
    :param parent_id: id родителя добавленого пакета
    :param ea_quid: уникальный ключ
    :return: экземпляр на основе полученных данных
    """
    logger = logging.getLogger("AddObject")
    with connection.cursor() as cursor:
        logger.info("Insert Object...")#добавление объекта
        if (ea_quid == '' or ea_quid == None):
            ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        sql = "INSERT INTO `t_object` (`Object_Type`, `Name`, `ea_guid`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`, `ModifiedDate`) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (object_type, name, ea_quid, stereotype, parent_id, package_id, created_date, created_date))
        result = get_by_ea_guid(ea_quid)
    connection.commit()
    logger.info(result)
    return result

def get_by_ea_guid(ea_guid):
    """
    Получение по уникальному ключу
    :param ea_guid: уникальный ключ
    :return: экземпляра по уникальному ключу
    """
    sql = "SELECT `Object_ID`, `Name`, `Stereotype`, `Package_ID`, `PDATA1`, `CreatedDate`, `ModifiedDate`  FROM `t_object` WHERE `ea_guid`=?" #поиск объекта по ключу
    result = connection.cursor().execute(sql, (ea_guid)).fetchall()
    return result

def get_by_id(object_id):
    """
    Получить по id экземпляра
    :param object_id: id объекта
    :return:
    """
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Stereotype`, `Name`, `PDATA1` FROM `t_object` WHERE `Object_ID`=?"  # проверка что данные изменились
        result = cursor.execute(sql, (object_id)).fetchall()
        if (result == []):
            return False
        else:
            return result


def update_object(name, stereotype, object_id):
    """
    Изменение данных объекта
    :param name: имя объекта
    :param stereotype: стереотип объекта
    :param object_id: id объекта
    :return: экземпляр измененного объекта
    """
    logger = logging.getLogger("UpdateObject")
    with connection.cursor() as cursor:
        modified_date = str(datetime.datetime.today())
        logger.info("Update object...")
        sql = "UPDATE `t_object` SET `Name`=?, `Stereotype`=?, `ModifiedDate`=? WHERE `Object_ID`=?" #поиск объекта по id и обновление нужных полей
        result = cursor.execute(sql, (name, stereotype, modified_date, object_id))
    connection.commit()
    result = get_by_id(object_id)
    if (result == False):
        logger.error("Doesn't exist such object id")
    else:
        print(result)
        logger.info(result)
    return result

def delete_by_ea_guid(ea_guid):
    """
    Удаление по ключу
    :param ea_guid:
    :return:
    """
    with connection.cursor() as cursor:
        sql = "DELETE FROM `t_object` WHERE `ea_guid`=?"
        result = get_by_ea_guid(ea_guid)
        cursor.execute(sql, (ea_guid))
        # поиск по уникальному ключу добавленного элемента
    connection.commit()
    return result