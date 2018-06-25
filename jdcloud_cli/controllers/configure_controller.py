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

from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.config import Config, ProfileManager


class ConfigureController(BaseController):
    class Meta:
        label = 'configure'
        help = '使用该子命令配置CLI'
        description = '配置 CLI 子命令，可以使用该子命令配置鉴权和区域等信息'
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--access-key'], dict(help='access key', dest='access_key', required=True)),
            (['--secret-key'], dict(help='secret key', dest='secret_key', required=True)),
            (['--region-id'], dict(help='region id', default='cn-north-1', dest='region_id', required=False)),
            (['--endpoint'], dict(help='api gateway endpoint', default='www.jdcloud-api.com', required=False)),
            (['--scheme'], dict(help='http scheme', default='https', required=False)),
            (['--timeout'], dict(help='request timeout', type=int, default=20, required=False)),
            (['--profile'], dict(help='profile name', default='default', required=False)),
        ],
        help='配置CLI运行环境，包括 access key, secret key 和区域等信息',
        description='配置CLI运行环境，包括 access key, secret key 和区域等信息。'
                    '示例：jdc configure add --profile test --access-key xxx --secret-key xxx --region-id cn-north-1 '
                    '--endpoint www.jdcloud-api.com --scheme https --timeout 20'
    )
    def add(self):
        access_key = self.app.pargs.access_key
        secret_key = self.app.pargs.secret_key
        region_id = self.app.pargs.region_id
        endpoint = self.app.pargs.endpoint
        scheme = self.app.pargs.scheme
        timeout = self.app.pargs.timeout
        profile = self.app.pargs.profile
        profile_manager = ProfileManager()
        result, msg = profile_manager.add_profile(profile,
                                                  Config(access_key, secret_key, region_id, endpoint, scheme, timeout))
        if result:
            print 'Configure successfully!'
        else:
            print msg

    @expose(
        arguments=[
            (['--profile'], dict(help='配置组名称', required=True)),
        ],
        help='删除某个配置组',
        description='删除某个配置组。示例：jdc configure delete --profile test'
    )
    def delete(self):
        profile_manager = ProfileManager()
        result, msg = profile_manager.delete_profile(self.app.pargs.profile)
        if result:
            print 'Configure successfully!'
        else:
            print msg

    @expose(
        arguments=[
            (['--profile'], dict(help='配置组名称', required=True)),
        ],
        help='切换到某个配置组',
        description='切换到某个配置组。示例：jdc configure use --profile default'
    )
    def use(self):
        profile_manager = ProfileManager()
        result, msg = profile_manager.set_current_profile(self.app.pargs.profile)
        if result:
            print 'Configure successfully!'
        else:
            print msg

    @expose(
        help='显示当前配置组',
        description='显示当前配置组。示例：jdc configure show-current'
    )
    def show_current(self):
        profile_manager = ProfileManager()
        profiles = profile_manager.get_current_profile()
        self._print_profiles(profiles)

    @expose(
        help='显示所有配置组',
        description='显示所有配置组。示例：jdc configure show-all'
    )
    def show_all(self):
        profile_manager = ProfileManager()
        profiles = profile_manager.get_all_profiles()
        self._print_profiles(profiles)

    def _print_profiles(self, profiles):
        for profile in profiles.keys():
            items = profiles[profile]
            print '================= %s ================' % profile
            for item in items:
                print '%s:  \t%s' % (item[0], item[1])