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

import os
import json
import yaml


class Skeleton(object):

    def __init__(self, service, api):
        self.__service = service
        self.__api = api

    def show(self):
        project_dir = os.path.dirname(os.path.abspath(__file__))
        json_file = '%s/resources/skeletons/%s.json' % (project_dir, self.__service)
        obj = yaml.load(open(json_file).read())

        if self.__api in obj:
            print(json.dumps(obj[self.__api], indent=4))
        else:
            print(self.__api + ' skeleton is not ready')


def show_skeleton(enable, service, api):
    if enable:
        skeleton = Skeleton(service, api)
        skeleton.show()
        return True

    return False
