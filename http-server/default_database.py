import mysql.connector
from os import environ


def default_connect():
    con = mysql.connector.connect(host=environ["DB_HOST"], user="root",
                                 password=environ["MYSQL_ROOT_PASSWORD"], database=environ["MYSQL_DATABASE"])
    if con.is_connected():
        cur = con.cursor()
        return (con, cur)
    raise mysql.connector.Error


def default_getEntries(db: tuple, arg='') -> list:  # Получение записей из базы данных
    con, cur = db
        
    cur.execute(f"SELECT * FROM data WHERE name LIKE '%{arg}%' ORDER BY name ASC")
    result = cur.fetchall()
    
    return result
