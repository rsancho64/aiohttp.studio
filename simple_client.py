#!/usr/bin/python3

import aiohttp
import asyncio

url = 'https://www.google.com/search?q=jamon'

async def main():
    """ mi primera corrutina en python"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            data = await response.text()
            print(data)

# asyncio.set_event_loop(asyncio.new_event_loop())

asyncloopEvent = asyncio.new_event_loop()
asyncio.set_event_loop(asyncloopEvent)
asyncloopEvent.run_until_complete(main())