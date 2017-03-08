#!/usr/bin/env python
# Author: Ocean <yousangdandan@yeah.net>

# Created Time: 日  3/ 5 17:47:22 2017
# coding=utf-8
## Last Modified : 一  3 06 11:20:37 2017

from japronto import Application


app = Application()
r = app.router


# Requests with the path set exactly to '/' and whatever method
# will be directed here.
def slash(request):
    return request.Response(text='Hello {} /!'.format(request.method))


r.add_route('/', slash)


# Requests with the path set exactly to '/love' and the method
# set exactly to 'GET' will be directed here.
def get_love(request):
    return request.Response(text='Got some love')

r.add_route('/love', get_love, 'GET')

# Requests with the path set exactly to '/methods' and the method
# set to 'POST' or 'DELETE' will be directed here.
def methods(request):
    return request.Response(text=request.method)


r.add_route('/methods', methods, methods=['POST', 'DELETE'])


# Requests with the path starting with '/params' segment and followed
# by two additional segments will be directed here.
# Values of the additional segments will be stored inside 'request.match_dict'
# dictionary with keys taken from {} placeholders. A request to '/params/1/2'
# would leave 'match_dict' set to '{'p1': 1, 'p2': '2'}'.
def params(request):
    return request.Response(text=str(request.match_dict))


r.add_route('/params/{p1}/{p2}', params)

app.run(debug=True)
