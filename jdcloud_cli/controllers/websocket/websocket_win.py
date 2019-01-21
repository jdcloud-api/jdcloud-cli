# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import msvcrt
import select
import sys
import websocket
import threading
from .websocket_base import WebsocketBase


class WebsocketWin(WebsocketBase):

    def get_win_size(self):
        res = None
        try:
            from ctypes import windll, create_string_buffer
            # stdin handle is -10
            # stdout handle is -11
            # stderr handle is -12
            h = windll.kernel32.GetStdHandle(-12)
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        except:
            return None

        if res:
            import struct
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey

    def invoke_shell(self, url, header):
        shell = websocket.create_connection(url, timeout=10, header=header)
        shell.send_binary('\n')

        threading.Thread(target=show_response, args=(shell,)).start()
        try:
            while True:
                x = msvcrt.getch()
                shell.send_binary(x)
        except websocket.WebSocketConnectionClosedException as e:
            print(e.message)
        except websocket.WebSocketException as e:
            print(e.message)


def show_response(shell):
    try:
        while True:
            r, w, e = select.select([shell.sock], [], [])
            if shell.sock in r:
                data = shell.recv()
                if data is None:
                    continue

                sys.stdout.write(data)
                sys.stdout.flush()
    except websocket.WebSocketConnectionClosedException as e:
        print(e.message)
    except websocket.WebSocketException as e:
        print(e.message)
