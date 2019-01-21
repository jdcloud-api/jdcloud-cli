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

import abc
import yaml
import sys


class InputJsonParser(object):

    def __init__(self, input_json):
        self.input_json = input_json

    @abc.abstractmethod
    def get_param_obj(self):
        pass


class JsonStringParser(InputJsonParser):

    def __init__(self, input_json):
        super(JsonStringParser, self).__init__(input_json)

    def get_param_obj(self):
        try:
            return yaml.load(self.input_json)
        except yaml.YAMLError:
            print('Json is invalid!')
            sys.exit(1)


class JsonFileParser(InputJsonParser):

    def __init__(self, input_json):
        super(JsonFileParser, self).__init__(input_json)

    def get_param_obj(self):
        file_path = self.input_json.replace('file://', '')
        try:
            with open(file_path) as f:
                content = f.read()
            return yaml.load(content)
        except IOError:
            print('File is not accessible!')
            sys.exit(1)
        except yaml.YAMLError:
            print('Json is invalid!')
            sys.exit(1)


def get_input_json_parser(input_json):
    if input_json.startswith('file://'):
        return JsonFileParser(input_json)
    else:
        return JsonStringParser(input_json)
