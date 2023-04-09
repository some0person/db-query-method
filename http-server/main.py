from aiohttp import web
from database import *


routes = web.RouteTableDef()


@routes.get('/')
async def response(request):
    db = await connect()
    fill = request.rel_url.query.get('fill', '')
    
    if fill:
        await addEntries(db)
        return web.Response(text="Successfully filled")
    
    search = request.rel_url.query.get('s', '')
    part = request.rel_url.query.get('p', '0')
    data = await getEntries(db, arg=search, part=part)
    s = f'Число результатов: {len(data)}\n\n'
    for line in data:
        s += " | ".join(list(map(str, line)))
        s += '\n'
        
    return web.Response(text=s)


app = web.Application()
app.add_routes(routes)
print("Server now running!")
web.run_app(app)