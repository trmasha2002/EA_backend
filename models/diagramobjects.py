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
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT MAX(`Instance_ID`) FROM `t_diagramobjects`" #взятие последнего добавленого элемента
        result = cursor.execute(sql).fetchall()[0]
        instance_id = result
        sql = "SELECT `Instance_ID`, `Object_ID`, `Diagram_ID` FROM `t_diagramobjects` WHERE `Instance_ID`=?" #поиск последнего добавленого элемента
        result = cursor.execute(sql, (instance_id)).fetchall()
        print(result)
        logger.info(result)
    connection.close()
    return result

