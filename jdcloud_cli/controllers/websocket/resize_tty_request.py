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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.printer import Printer


class ResizeTtyRequest(JDCloudRequest):

    def __init__(self, parameters, header=None, version="v1"):
        super(ResizeTtyRequest, self).__init__('/regions/{regionId}/containers/{containerId}:resizeTTY',
                                               'POST', header, version)
        self.parameters = parameters


def resize_tty(h, w, app, region_id, container_id, exec_id=None):
    params = {'height': h, 'width': w, 'regionId': region_id, 'containerId': container_id}
    if exec_id is not None:
        params.update({'execId': exec_id})

    client_factory = ClientFactory('nc')
    client = client_factory.get(app)
    if client is None:
        return

    req = ResizeTtyRequest(params)
    resp = client.send(req)
    Printer.print_result(resp)