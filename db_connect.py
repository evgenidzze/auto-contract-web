import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Lbgkjv19'
)


cursor_obj = dataBase.cursor()
cursor_obj.execute("CREATE DATABASE auto_contract")
