"""
Brython MDCFramework: Radiant
=============================

"""

import random
from browser import ajax, window, websocket, document, timer
import json


########################################################################
class LocalInterpreter:
    """AndroidMain

    Connect with app
    """

    # ----------------------------------------------------------------------
    def __init__(self, url=None, csrftoken=None):
        """Constructor"""

        self.url_ = url

        if csrftoken:
            self.csrftoken = csrftoken

        elif hasattr(window, 'csrftoken'):
            self.csrftoken = window.csrftoken
        else:
            self.csrftoken = "NO_CSRFTOKEN_PROVIDED"

        if url is None:
            # try:
                # self.url_ = '/'
                # self.test()
            # except:
            self.url_ = '/python_handler'
            self.test()

    # ----------------------------------------------------------------------
    def __getattr__(self, attr):
        """"""
        if attr.endswith('_async'):
            attr = attr.replace('_async', '')
            f = lambda *args, **kwargs: self.__request_async__(
                attr, *args, **kwargs)
        else:
            f = lambda *args, **kwargs: self.__request__(
                attr, *args, **kwargs)

        f.__name__ = attr
        return f

    # ----------------------------------------------------------------------
    def __request__(self, attr, *args, **kwargs):
        """"""
        req = ajax.ajax()
        req.open('POST', self.url_, False)
        req.set_header('content-type', 'application/x-www-form-urlencoded')
        req.send({'name': attr, 'args': json.dumps(list(args)), 'kwargs': json.dumps(kwargs),
                  'csrfmiddlewaretoken': self.csrftoken})

        try:
            resp = json.loads(req.text)['__RDNT__']
        except:
            resp = req.text

        return resp

    # ----------------------------------------------------------------------
    def __request_async__(self, attr, *args, **kwargs):
        """"""
        def __ajax__(fn):
            req = ajax.ajax()
            req.bind('complete', fn)
            req.open('POST', self.url_, True)
            req.set_header(
                'content-type', 'application/x-www-form-urlencoded')
            req.send({'name': attr, 'args': json.dumps(list(args)), 'kwargs': json.dumps(kwargs),
                      'csrfmiddlewaretoken': self.csrftoken})

        return __ajax__


########################################################################
class WebSocket:
    """WebSocket

    COnnectt with app

    """
    # ----------------------------------------------------------------------
    def __init__(cls, ip):
        """"""
        if not websocket.supported:
            print("WebSocket is not supported by your browser")
            return
        cls.ip_ = ip
        # open a web socket
        # cls.ws = websocket.WebSocket("wss://192.168.1.20:8888")
        cls.ws = websocket.WebSocket(ip)
        # bind functions to web socket events
        cls.ws.bind('open', cls.on_open)
        cls.ws.bind('error', cls.on_error)
        cls.ws.bind('message', cls.on_message)
        cls.ws.bind('close', cls.on_close)

        port_ip = ip.replace('wss://', '').replace('ws://',
                                                   '').replace('/ws', '')

        # cls.ip = port_ip[:port_ip.find(":")]
        # cls.port =  port_ip[port_ip.find(":")+1:]
        cls.ip = port_ip
        cls.protocol = 'wss' if 'wss' in ip else 'ws'

    # ----------------------------------------------------------------------
    def on_open(cls, evt):
        """"""
        # print('ON OPEN')

    # ----------------------------------------------------------------------
    def on_error(cls, evt):
        """"""
        # print('ON ERROR')

    # ----------------------------------------------------------------------
    def on_message(cls, evt):
        """"""
        # print('ON MESSAGE')

    # ----------------------------------------------------------------------
    def on_close(cls, evt):
        """"""
        # print('ON CLOSE')

    # ----------------------------------------------------------------------
    def send(cls, data):
        """"""
        cls.wait_for_connection(cls._send, data)

    # ----------------------------------------------------------------------
    def wait_for_connection(cls, callback, data):
        """"""
        if cls.ws.readyState == 1:
            return callback(data)
        else:
            timer.set_timeout(lambda: cls.wait_for_connection(
                callback, data), 1000)

    # ----------------------------------------------------------------------
    def _send(cls, data):
        """"""
        if not data:
            return

        if isinstance(data, (str, bytes)):
            cls.ws.send(data)
        else:
            data = json.dumps(data)
            cls.ws.send(data)

    # ----------------------------------------------------------------------
    def close_connection(cls, *args, **kwargs):
        """"""
        cls.ws.close()


# ########################################################################
# class API:
    # """"""

    # # ----------------------------------------------------------------------
    # def __init__(self, url, auth=None, token=None, csrftoken=None, append_slash=True):
        # """Constructor"""
        # self.url_ = url
        # self.url_ = self.url_.strip('/')

        # self.token = token

        # if csrftoken:
            # self.csrftoken = csrftoken

        # elif hasattr(window, 'csrftoken'):
            # self.csrftoken = window.csrftoken
        # else:
            # self.csrftoken = None

        # self.append_slash = append_slash

    # # ----------------------------------------------------------------------
    # def head(self, endpoint):
        # """"""
        # return self.__request__('HEAD', f'{self.url_}/{endpoint}')

    # # ----------------------------------------------------------------------
    # def get(self, endpoint, pk=None, data=None):
        # """"""
        # if pk:
            # return self.__request__('GET', f'{self.url_}/{endpoint}/{pk}', data)
        # else:
            # return self.__request__('GET', f'{self.url_}/{endpoint}', data)

    # # ----------------------------------------------------------------------
    # def delete(self, endpoint, pk, data=None):
        # """"""
        # return self.__request__('DELETE', f'{self.url_}/{endpoint}/{pk}', data)

    # # ----------------------------------------------------------------------
    # def post(self, endpoint, data=None):
        # """"""
        # return self.__request__('POST', f'{self.url_}/{endpoint}', data)

    # # ----------------------------------------------------------------------
    # def patch(self, endpoint, pk, data=None):
        # """"""
        # return self.__request__('PATCH', f'{self.url_}/{endpoint}/{pk}', data)

    # # ----------------------------------------------------------------------
    # def options(self, endpoint, data=None):
        # """"""
        # return self.__request__('OPTIONS', f'{self.url_}/{endpoint}', data)

    # # ----------------------------------------------------------------------
    # def __request__(self, method, url, data=None):
        # """"""
        # req = ajax.ajax()

        # if self.append_slash:
            # url = f'{url.strip("/")}/'

        # req.open(method, url, False)

        # req.setRequestHeader('content-type', 'application/json')

        # if self.token:
            # req.set_header('Authorization', f"JWT {self.token}")

        # if self.csrftoken:
            # req.setRequestHeader('X-CSRFToken', self.csrftoken)

        # if data:
            # data = json.dumps(data)
            # req.send(data)
        # else:
            # req.send()

        # data = json.loads(req.text)
        # return data


# # ----------------------------------------------------------------------
# def get(url, method="GET", csrftoken=None):
    # """"""
    # if csrftoken:
        # csrftoken = csrftoken

    # elif hasattr(window, 'csrftoken'):
        # csrftoken = window.csrftoken
    # else:
        # csrftoken = None

    # req = ajax.ajax()
    # req.open(method, url, False)
    # req.set_header('content-type', 'application/x-www-form-urlencoded')
    # req.send({'csrfmiddlewaretoken': csrftoken})
    # return json.loads(req.text)


# # ----------------------------------------------------------------------
# def gen_id(length=8, charset='abcdefghijklmnopqrstuvwxyz123456789'):
    # """"""
    # return ''.join([random.choice(charset) for n in range(length)])


# ----------------------------------------------------------------------
def autoinit():
    """"""
    window.mdc.autoInit()
    try:
        [window.mdc.slider.MDCSlider.attachTo(
            slider) for slider in document.select('.mdc-slider')]
    except:
        pass


# ----------------------------------------------------------------------
def autoiframe(id_, parent):
    """"""
    if iframe := document.select_one(f'#{id_}'):
        if iframe.contentWindow.document.select_one(parent):
            iframe.style.height = f"{iframe.contentWindow.document.documentElement.scrollHeight}px"
            return timer.set_timeout(lambda: autoiframe(id_, parent), 2000)
    timer.set_timeout(lambda: autoiframe(id_, parent), 500)


class fake:
    def __getattr__(self, attr):
        return None
