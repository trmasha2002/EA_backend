import pymysql.cursors


class Connection:
    def __init__(self):
        self.connect = pymysql.connect(host='localhost',
                                       user='root',
                                       password='root',
                                       db='easample',
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
