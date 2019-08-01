import pymysql


def add_diagramobjects(diagram_id, object_id):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        sql = "INSERT INTO `t_diagramobjects` (`Object_ID`, `Diagram_ID`) VALUES (%s, %s)"
        cursor.execute(sql, (object_id, diagram_id))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT `Object_ID`, `Diagram_ID` FROM `t_diagramobjects` WHERE `Object_ID`=%s"
        cursor.execute(sql, (object_id))
        result = cursor.fetchone()
        print(result)
    connection.close()


add_diagramobjects('100', '101')