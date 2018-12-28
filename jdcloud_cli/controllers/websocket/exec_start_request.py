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

from jdcloud_sdk.core.signer import Signer
from jdcloud_sdk.core.credential import Credential
from jdcloud_cli.utils import encode_jdcloud_headers
from jdcloud_cli.config import ProfileManager
from jdcloud_cli.const import WEBSOCKET_SCHEME, METHOD_GET
from jdcloud_cli.logger import get_logger
from jdcloud_cli.controllers.websocket.resize_tty_request import resize_tty
from jdcloud_cli.controllers.websocket.websocket_base import web_socket


class ExecStartRequest(object):

    def __init__(self, service, scheme, endpoint, method, headers, region_id, container_id, exec_id, pod_id=None):
        url_map = {'nc': '%s://%s/v1/regions/%s/containers/%s:execStart?execId=%s' % (scheme, endpoint, region_id, container_id, exec_id),
                   'pod': '%s://%s/v1/regions/%s/pods/%s/containers/%s:execStart?execId=%s' % (scheme, endpoint, region_id, pod_id, container_id, exec_id)}
        self.__url = url_map[service]
        self.__method = method
        self.__region_id = region_id
        self.__service = service
        self.__headers = {'content-type': 'application/json'}
        if headers is not None:
            self.__headers.update(headers)
            encode_jdcloud_headers(self.__headers)

    def invoke_shell(self, credential):
        singer = Signer(get_logger(False))
        singer.sign(self.__method, self.__service, self.__region_id, self.__url, self.__headers, '', credential, '')
        web_socket.invoke_shell(self.__url, self.__headers)


def exec_start(app, service, headers, region_id, container_id, exec_id, pod_id=None):
    def handle_signal(signum, frame):
        h, w = web_socket.get_win_size()
        resize_tty(h, w, app, service, headers, region_id, container_id, exec_id)

    web_socket.reg_winch_handler(handle_signal)

    profile_manager = ProfileManager()
    cli_config = profile_manager.load_current_profile()
    credential = Credential(cli_config.access_key, cli_config.secret_key)
    request = ExecStartRequest(service, WEBSOCKET_SCHEME, cli_config.endpoint, METHOD_GET, headers, region_id, container_id, exec_id, pod_id=pod_id)
    request.invoke_shell(credential)

    h_o, w_o = web_socket.get_win_size()
    resize_tty(h_o, w_o, app, service, headers, region_id, container_id, exec_id, pod_id=pod_id)
