#!/usr/bin/env python
# Author: Ocean <yousangdandan@yeah.net>

# Created Time: 日  3/ 5 16:31:37 2017
# coding=utf-8
## Last Modified : 日  3 05 16:41:19 2017

from japronto import Application

def hello(request):
    return request.Response(text='Hello world!')


app = Application()
app.router.add_route('/', hello)
app.run(debug=True)
