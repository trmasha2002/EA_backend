from connection import connection
import logging
def add_diagramobjects(diagram_id, object_id):
    """
    Создание объекта диаграммы на основе полученных данных
    :param diagram_id: id диаграмы
    :param object_id: id объекта
    :return: экземпляр диаграммы на основе полученных данных
    """
    logger = logging.getLogger("AddDiagramObjects")
    with connection.cursor() as cursor:
        logger.info("Insert DiagramObject...")
        sql = "INSERT INTO `t_diagramobjects` (`Object_ID`, `Diagram_ID`) VALUES (?, ?)"#добавление объекта
        cursor.execute(sql, (object_id, diagram_id))
        sql = "SELECT MAX(`Instance_ID`) FROM `t_diagramobjects`"  # взятие последнего добавленого элемента
        result = cursor.execute(sql).fetchall()[0][0]
        instance_id = result
    connection.commit()
    result = get_by_id(instance_id)
    logger.info(result)
    connection.close()
    return result
def get_by_id(instance_id):
    with connection.cursor() as cursor:
        sql = "SELECT `Instance_ID`, `Object_ID`, `Diagram_ID` FROM `t_diagramobjects` WHERE `Instance_ID`=?" #поиск последнего добавленого элемента
        result = cursor.execute(sql, (instance_id)).fetchall()
    return result


def delete_by_ea_instance_id(instance_id):
    with connection.cursor() as cursor:
        sql = "DELETE FROM `t_diagramobjects` WHERE `Instance_ID`=?"
        result = get_by_id(instance_id)# поиск по уникальному ключу добавленного элемента
        cursor.execute(sql, (instance_id))
    connection.commit()
    return result