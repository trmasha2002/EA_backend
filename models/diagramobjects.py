import pymysql


def add_diagramobjects(diagram_id, object_id):
    connection = pymysql.connect(host='localhost', #подключение к базе данных
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        sql = "INSERT INTO `t_diagramobjects` (`Object_ID`, `Diagram_ID`) VALUES (%s, %s)"#добавление объекта
        cursor.execute(sql, (object_id, diagram_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT MAX(`Instance_ID`) FROM `t_diagramobjects`" #взятие последнего добавленого элемента
        cursor.execute(sql)
        result = cursor.fetchone()
        instance_id = str(result['MAX(`Instance_ID`)'])
        sql = "SELECT `Instance_ID`, `Object_ID`, `Diagram_ID` FROM `t_diagramobjects` WHERE `Instance_ID`=%s" #поиск последнего добавленого элемента
        cursor.execute(sql, (instance_id))
        result = cursor.fetchone()
        print(result)
    connection.close()
    return result

