#!/usr/bin/env python
# Author: Ocean <yousangdandan@yeah.net>

# Created Time: 日  3/ 5 16:52:25 2017
# coding=utf-8
## Last Modified : 日  3 05 17:45:12 2017

import asyncio
from japronto import Application


# This is a synchronous handler.
def synchronous(request):
    return request.Response(text='I am synchronous!')


# This is an asynchronous handler. It spends most of the time in the event loop.
# It wakes up every second 1 to print and finally returns after 3 seconds.
# This lets other handlers execute in the same processes while
# from the point of view of the client it took 3 seconds to complete.
async def asynchronous(request):
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(i, 'seconds elapsed')

    return request.Response(text='3 seconds elapsed')


app = Application()

r = app.router
r.add_route('/sync', synchronous)
r.add_route('/async', asynchronous)

app.run(debug=True)
