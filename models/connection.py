import pymysql.cursors

connection = pymysql.connect(host='localhost',
                                       user='root',
                                       password='root',
                                       db='easample',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
