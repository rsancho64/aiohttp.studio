#!/usr/bin/python3

import aiohttp
import asyncio

async def get_async(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)

urls = [
    'http://webcode.me',
    'https://httpbin.org/get',
    'https://google.com',
    'https://tusalchichondirecto.com'  # :/ juas
    'https://stackoverflow.com',
    'https://github.com'
]

async def launch():
    """lanzadera lanzable asincrona que pide como un pobre"""
  
    # starred args...
    # "https://search.brave.com/search?q=python+starred+fucntion+what+is&source=desktop&summary=1&summary_og=c288132f45dbc693a32b5d  "

    # try ... https://superfastpython.com/asyncio-task-exceptions/
    try:
        resps = await asyncio.gather(*map(get_async, urls))
        stat = [resp.status for resp in resps]
    except # socket.gaierror
    except # ClientConnectorError

    for status_code in stat:
        print(status_code)

asyncio.run(launch())