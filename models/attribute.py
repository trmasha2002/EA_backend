import pymysql.cursors
import uuid


def add_attribute(name, object_id):
    connection = pymysql.connect(host='localhost',  #подключение к базе данных
                                 user='root',
                                 password='root',
                                 db='easample',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        ea_quid = '{' + str(uuid.uuid4()) + '}'#генерация уникального ключа
        sql = "INSERT INTO `t_attribute` (`Object_ID`, `ea_guid`, `Name`) VALUES (%s, %s, %s)" #добавление в таблицу
        cursor.execute(sql, (object_id, ea_quid, name))
    connection.commit()
    with connection.cursor() as cursor:
        sql = "SELECT  `ID`, `Object_ID`, `Name` FROM `t_attribute` WHERE `ea_guid`=%s" #поиск по уникальному ключу добавленного элемента
        cursor.execute(sql, (ea_quid))
        result = cursor.fetchone()
        print(result)
    connection.close()
    return result

