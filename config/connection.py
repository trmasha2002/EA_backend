import pymysql.cursors
import pyodbc

connection = pyodbc.connect("Driver={Devart ODBC Driver for MySQL};"
                            "Server=localhost;"
                            "Database=easample;"
                            "USER=root;"
                            "PASSWORD=root;"
                            "OPTION=3;")