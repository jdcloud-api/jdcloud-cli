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
from configparser import SafeConfigParser

CONF_AK = 'access_key'
CONF_SK = 'secret_key'
CONF_REGION = 'region_id'
CONF_ENDPOINT = 'endpoint'
CONF_SCHEME = 'scheme'
CONF_TIMEOUT = 'timeout'


class Config(object):

    def __init__(self, access_key, secret_key, region_id, endpoint, scheme, timeout):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region_id = region_id
        self.endpoint = endpoint
        self.scheme = scheme
        self.timeout = timeout


class ProfileManager(object):

    def __new__(type):
        if '_instance' not in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def __init__(self):
        cli_dir = self.__make_config_dir()
        self.__config_file = cli_dir + '/config'
        self.__current_file = cli_dir + '/current'
        self.__current_profile_name = self.__get_current_profile_name()
        self.__parser = SafeConfigParser()
        self.__parser.read(self.__config_file)

    def load_current_profile(self):
        if self.__current_profile_name not in self.__parser.sections():
            print('Please use `jdc configure add` command to add cli configure first.')
            return None

        # notice that the type of config info which read from file is unicode
        # python SDK uses type str
        access_key = str(self.__parser.get(self.__current_profile_name, CONF_AK))
        secret_key = str(self.__parser.get(self.__current_profile_name, CONF_SK))
        region_id = str(self.__parser.get(self.__current_profile_name, CONF_REGION))
        endpoint = str(self.__parser.get(self.__current_profile_name, CONF_ENDPOINT))
        scheme = str(self.__parser.get(self.__current_profile_name, CONF_SCHEME))
        timeout = self.__parser.get(self.__current_profile_name, CONF_TIMEOUT) \
            if CONF_TIMEOUT in self.__parser.items(self.__current_profile_name,) else 20
        return Config(access_key, secret_key, region_id, endpoint, scheme, timeout)

    def get_all_profiles(self):
        result = dict()
        sections = self.__parser.sections()
        for section in sections:
            result[section] = self.__parser.items(section)
        return result

    def get_current_profile(self):
        result = dict()
        if not self.__parser.has_section(self.__current_profile_name):
            return result

        result[self.__current_profile_name] = self.__parser.items(self.__current_profile_name)

        return result

    def add_profile(self, profile, config):
        if self.__parser.has_section(profile):
            return False, 'Profile ' + profile + ' has existed'

        self.__parser.add_section(profile)

        # use enums for the fields order
        for key in [CONF_AK, CONF_SK, CONF_REGION, CONF_ENDPOINT, CONF_SCHEME, CONF_TIMEOUT]:
            value = config.__dict__[key]
            self.__parser.set(profile, key, str(value))

        return self.__write_config_file()

    def delete_profile(self, profile):
        if not self.__parser.has_section(profile):
            return False, 'No profile ' + profile

        if profile == self.__current_profile_name:
            return False, 'Can not delete current profile: ' + profile

        self.__parser.remove_section(profile)
        return self.__write_config_file()

    def set_current_profile(self, name):
        if not self.__parser.has_section(name):
            return False, 'Profile %s do not exist! Configure failed!' % name
        try:
            with open(self.__current_file, 'w') as f:
                f.write(name)
            self.__current_profile_name = name
        except Exception as e:
            return False, e
        return True, ''

    def __write_config_file(self):
        try:
            with open(self.__config_file, 'w+') as f:
                self.__parser.write(f)
        except Exception as e:
            return False, e
        return True, ''

    def __make_config_dir(self):
        home = os.path.expanduser("~")
        cli_dir = home + "/.jdc"
        if not os.path.exists(cli_dir):
            os.makedirs(cli_dir)
        return cli_dir

    def __get_current_profile_name(self):
        if not os.path.exists(self.__current_file):
            with open(self.__current_file, 'w') as f:
                f.write('default')
            return 'default'

        with open(self.__current_file, 'r') as f:
            name = f.read()
        return name
