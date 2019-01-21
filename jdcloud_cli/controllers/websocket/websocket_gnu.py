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

import sys
import termios
import tty
import select
import signal
import json
import errno
import struct
import fcntl
import websocket
from .websocket_base import WebsocketBase
from jdcloud_cli.utils import decode


class WebsocketGnu(WebsocketBase):

    def reg_winch_handler(self, handler):
        signal.signal(signal.SIGWINCH, handler)

    def get_win_size(self):
        s = struct.pack('HHHH', 0, 0, 0, 0)
        t = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s)
        h, w, hp, wp = struct.unpack('HHHH', t)
        return h, w

    def invoke_shell(self, url, header):
        shell = websocket.create_connection(url, timeout=10, header=header)
        oldtty = None
        try:
            oldtty = termios.tcgetattr(sys.stdin)
        except:
            pass

        old_handler = signal.getsignal(signal.SIGWINCH)

        try:
            if oldtty:
                tty.setraw(sys.stdin.fileno())
                tty.setcbreak(sys.stdin.fileno())

            while True:
                try:
                    if oldtty:
                        r, w, e = select.select([shell.sock, sys.stdin], [], [shell.sock], 5)
                        if sys.stdin in r:
                            x = sys.stdin.read(1)
                            # read arrows
                            if x == '\x1b':
                                x += sys.stdin.read(1)
                                if x[1] == '[':
                                    x += sys.stdin.read(1)
                            if len(x) == 0:
                                shell.send_binary('\n')
                            shell.send_binary(x)
                    else:
                        x = str(sys.stdin.read())
                        r, w, e = select.select([shell.sock], [], [shell.sock], 1)
                        shell.send_binary(x)
                        shell.send_binary(u"\u0004")

                    if shell.sock in r:
                        data = shell.recv()
                        if not data:
                            continue
                        try:
                            message = json.loads(data)
                            if message.get("type") == "error":
                                print(message)
                                raise Exception
                            streamType = message.get("streamType")
                            if streamType == "stdout":
                                sys.stdout.write(message.get("output"))
                                sys.stdout.flush()
                            elif streamType == "stderr":
                                sys.stderr.write(message.get("output"))
                                sys.stderr.flush()
                        except:
                            sys.stdout.write(decode(data))
                            sys.stdout.flush()
                except (select.error, IOError) as e:
                    if e.args and e.args[0] == errno.EINTR:
                        pass
                    else:
                        raise
        except websocket.WebSocketConnectionClosedException as e:
            print(e)
        except websocket.WebSocketException as e:
            print(e)
        except Exception as e:
            sys.stderr.write("%s\r\n" % e)
            sys.stderr.flush()
        finally:
            if oldtty:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
            signal.signal(signal.SIGWINCH, old_handler)

