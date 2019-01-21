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

import yaml
import sys
from jdcloud_cli.inputjson_parser import get_input_json_parser
from jdcloud_cli.const import REGION_ID
from jdcloud_cli.config import ProfileManager


def collect_user_args(app):
    params_dict = _get_input_args(app.pargs.__dict__)

    if params_dict.get('input_json') is not None:
        parser = get_input_json_parser(app.pargs.input_json)
        input_dict = parser.get_param_obj()
        if input_dict is None:
            return None

        params_dict.update(input_dict)
    _append_region_id(params_dict)
    return params_dict


def collect_user_headers(app):
    headers = app.pargs.headers
    if headers is None:
        return None

    try:
        obj = yaml.load(headers)
        if not isinstance(obj, dict):
            raise yaml.YAMLError
    except yaml.YAMLError:
        print('user headers is not dict')
        exit(1)

    return obj


def _get_input_args(pargs_dict):
    result = dict()

    for key in pargs_dict.keys():
        if key.startswith('_') or key in ['suppress_output', 'debug', 'output', 'skeleton', 'headers']:
            continue

        dispatch = pargs_dict['__dispatch__'].replace('_', '-')
        if key == 'command' and dispatch.split('.')[-1] == pargs_dict[key]:
            continue

        value = pargs_dict[key]
        try:
            if isinstance(value, str) and (value.startswith('{') or value.startswith('[')):
                result[key] = _parse_json(value)
            else:
                result[key] = pargs_dict[key]
        except Exception:
            print('Parameter %s is invalid!' % key)
            sys.exit(1)
    return result


def _parse_json(string):
    try:
        obj = yaml.load(string)
        return obj
    except ValueError:
        return string


def _append_region_id(param_dict):
    if REGION_ID in param_dict and param_dict[REGION_ID] is None:
        pm = ProfileManager()
        param_dict.update({REGION_ID: str(pm.load_current_profile().region_id)})

