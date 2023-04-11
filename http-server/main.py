from aiohttp import web
from database import *


routes = web.RouteTableDef()


@routes.get('/')
async def response(request):  # Обработка запросов к асинхронному web-серверу
    db = await connect()
    fill = request.rel_url.query.get('fill', '')
    search = request.rel_url.query.get('s', '')
    part = request.rel_url.query.get('p', '0')
    
    if fill:
        await addEntries(db)
        return web.Response(text="Successfully filled")
    
    data = await getEntries(db, arg=search, part=part)
    s = "Использование:\n \
fill - заполнить базу данных на 40.000 записей \n \
s - поиск по строке\n \
p - часть результатов\n\n"
    s += f'Число результатов: {len(data)}\n\n'
    
    for line in data:
        s += " | ".join(list(map(str, line)))
        s += '\n'
        
    return web.Response(text=s)


app = web.Application()
app.add_routes(routes)
web.run_app(app)
