# main.py

import os
import uuid
import mimetypes
import falcon
import gevent
from gevent import socket
from controller.users import *
from controller.users_info import *
from controller.image import *

# falcon.API instances are callable WSGI apps
app = falcon.API()

# things will handle all requests to the '/things' URL path
app.add_route('/users', Users())
app.add_route('/user', User())
app.add_route('/user/{id}', User())
app.add_route('/user/email/{email}', UserEmail())
app.add_route('/login', Login())
app.add_route('/infos', UsersInfo())
app.add_route('/info', UserInfo())
app.add_route('/info/{id}', UserInfo())
app.add_route('/picture', Images())
app.add_route('/picture/{id}', Images())