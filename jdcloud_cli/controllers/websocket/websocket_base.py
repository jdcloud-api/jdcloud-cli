import abc
import os


class WebsocketBase(object):

    @abc.abstractmethod
    def get_win_size(self):
        pass

    @abc.abstractmethod
    def invoke_shell(self, url, header):
        pass

    @abc.abstractmethod
    def reg_winch_handler(self, handler):
        pass


def websocket_instance():
    if os.name != 'nt':
        from .websocket_gnu import WebsocketGnu
        return WebsocketGnu()
    else:
        from .websocket_win import WebsocketWin
        return WebsocketWin()


web_socket = websocket_instance()
