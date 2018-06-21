# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import signal
from jdcloud_sdk.core.signer import Signer
from jdcloud_sdk.core.credential import Credential
from jdcloud_cli.config import ProfileManager
from jdcloud_cli.const import WEBSOCKET_SCHEME, METHOD_GET
from jdcloud_cli.logger import get_logger
from jdcloud_cli.controllers.websocket.resize_tty_request import resize_tty
from jdcloud_cli.controllers.websocket.websocket_base import web_socket


class AttachRequest(object):

    def __init__(self, scheme, endpoint, method, region_id, container_id):
        self.__url = '%s://%s/v1/regions/%s/containers/%s:attach' % \
                     (scheme, endpoint, region_id, container_id)
        self.__method = method
        self.__headers = {'content-type': 'application/json'}
        self.__region_id = region_id

    def invoke_shell(self, credential):
        singer = Signer(get_logger(False))
        singer.sign(self.__method, 'nc', self.__region_id, self.__url, self.__headers, '', credential, '')
        web_socket.invoke_shell(self.__url, self.__headers)


def attach(app, region_id, container_id):
    def handle_signal(signum, frame):
        h, w = web_socket.get_win_size()
        resize_tty(h, w, app, region_id, container_id)

    web_socket.reg_winch_handler(handle_signal)

    profile_manager = ProfileManager()
    cli_config = profile_manager.load_current_profile()
    credential = Credential(cli_config.access_key, cli_config.secret_key)
    request = AttachRequest(WEBSOCKET_SCHEME, cli_config.endpoint, METHOD_GET, region_id, container_id)
    request.invoke_shell(credential)

    h_o, w_o = web_socket.get_win_size()
    resize_tty(h_o, w_o, app, region_id, container_id)
