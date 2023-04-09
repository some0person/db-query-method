import asyncio
import aiomysql
from os import environ
from datetime import datetime


loop = asyncio.get_event_loop()


async def connect():
    con = await aiomysql.connect(host=environ["DB_HOST"], user="root", password=environ["MYSQL_ROOT_PASSWORD"], db=environ["MYSQL_DATABASE"], loop=loop)
    cur = await con.cursor()
    return (con, cur)


async def getEntries(db: tuple, arg='', part='0') -> list:
    con, cur = db
    if not part.isdecimal():
        part = 0
    else:
        part = int(part)
        
    await cur.execute(f"SELECT date,name,url FROM (SELECT *,row_number() \
                           OVER (ORDER BY date ASC) AS rn FROM data WHERE name \
                           LIKE '%{arg}%') sub WHERE rn>='{part * 100}' AND rn<='{(part + 1) * 100}' ORDER BY rn ASC")
    result = await cur.fetchall()
    con.close()
    return result


async def addEntries(db: tuple) -> None:
    con, cur = db
    for i in range(40_000):
        await cur.execute("INSERT INTO data (date, name, url) VALUES (%s, %s, %s)", (datetime.now(), i, f"https://{i}.domain/link"))
    await con.commit()
    con.close()