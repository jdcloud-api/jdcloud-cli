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
import base64


def cmd_input(msg):
    if sys.version_info.major == 2:
        return raw_input(msg)
    elif sys.version_info.major == 3:
        return input(msg)


def encode(msg):
    if sys.version_info.major == 2:
        return msg.encode('utf8')
    elif sys.version_info.major == 3:
        return msg


def decode(msg):
    if sys.version_info.major == 2:
        return msg
    elif sys.version_info.major == 3:
        return msg.decode()


def encode_jdcloud_headers(headers):
    for k in headers.keys():
        if k in ['x-jdcloud-pin', 'x-jdcloud-erp', 'x-jdcloud-security-token']:
            headers[k] = base64.b64encode(headers[k])
