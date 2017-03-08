#!/usr/bin/env python
# Author: Ocean <yousangdandan@yeah.net>

# Created Time: 日  3/ 5 16:45:45 2017
# coding=utf-8
## Last Modified : 四  1 01 07:59:59 1970

from japronto import Application


# Views handle logic, take request as a parameter and return the Response object back to the client
def hello(request):
    return request.Response(text='Hello world!')


# The Application instance is a fundamental concept.
# It is a parent to all the resources and all the settings.
# can be tweeked there.
app = Application()


# The Router instance lets you register your handlers and execute
# them depending on the url path and methods.
app.router.add_route('/', hello)


# Finally, start our server and handle requests until termination is
# requested. Enabling debug lets you see request logs and stact traces.
app.run(debug=True)
