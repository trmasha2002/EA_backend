import pymysql.cursors

connect = pymysql.connect(host='localhost',  #подключение к базе данных
                                       user='root',
                                       password='root',
                                       db='easample',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
