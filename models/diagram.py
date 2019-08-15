import datetime
import uuid
from connection import connection
import logging
def add_diagram(name, package_id, stereotype, diagram_type):
    logger = logging.getLogger("AddDiagram")
    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}' #генерация уникального ключа
        created_date = str(datetime.datetime.today())
        logger.info("Add Diagram...")
        sql = "INSERT INTO `t_diagram` (`Package_ID`, `Name`, `ea_guid`, `Stereotype`, `Diagram_Type`,`CreatedDate`) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (package_id, name, ea_quid, stereotype, diagram_type, created_date)) #добавление элемента
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Diagram_ID`, `Name`, `Package_ID`, `Stereotype`, `Diagram_Type` FROM `t_diagram` WHERE `ea_guid`=?" #поиск по уникальному ключу
        result = cursor.execute(sql, (ea_quid)).fetchall()
        print(result)
        logger.info(result)
    connection.close()
    return result


