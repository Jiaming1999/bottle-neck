# -*- coding: utf-8 -*-
#
#    Copyright (C) 2015  Papavassiliou Vassilis
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""`bottle-neck` project.

Provides useful utilities for creating web-services with bottle.py
micro-framework.
"""

__author__ = 'Papavassiliou Vassilis'
__date__ = '2015-11-28'
__version__ = '0.0.1'

__all__ = ['BaseHandler', 'BaseHandlerPlugin', 'route_method', 'plugin_method',
           'HandlerError', 'HandlerPluginError', 'HandlerHTTPMethodError',
           'WSResponse', 'WSResponseException', 'Router', 'Route',
           'RouteError', 'BasePlugin', 'WrapErrorPlugin', 'BaseMiddleware',
           'StripPathMiddleware', 'cors_enable_hook', 'strip_path_hook']


from handlers import (
    BaseHandler, BaseHandlerPlugin, route_method, plugin_method, HandlerError,
    HandlerPluginError, HandlerHTTPMethodError
)
from response import (WSResponse, WSResponseException)
from routing import (RouteError, Router, Route)
from plugins import (BasePlugin, WrapErrorPlugin)
from middleware import (BaseMiddleware, StripPathMiddleware)
from webapi import (cors_enable_hook, strip_path_hook)
