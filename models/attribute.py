import uuid
import logging
from connection import connection
def add_attribute(name, object_id):
    logger = logging.getLogger("AddAttribute")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'#генерация уникального ключа
        logger.info("Insert attribute...")
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (?, ?, ?)" #добавление в таблицу
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT  `ID`, `Object_ID`, `Name` FROM `t_attribute` WHERE `ea_guid`=?" #поиск по уникальному ключу добавленного элемента
        result = cursor.execute(sql, (ea_quid)).fetchall()
        print(result)
        logger.info(result)
    connection.close()
    return result

