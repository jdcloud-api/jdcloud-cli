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

import json


class Printer(object):

    @staticmethod
    def print_result(resp):
        print json.dumps(resp.__dict__, cls=ErrorEncoder, indent=4, ensure_ascii=False)


class ErrorEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
