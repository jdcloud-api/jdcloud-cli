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
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class AmsController(BaseController):
    class Meta:
        label = 'ams'
        help = '京东云视频云应用管理平台接口（仅对授权用户使用）'
        description = '''
        ams cli 子命令，京东云视频云应用管理平台接口（仅对授权用户使用）。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--stream-id'], dict(help="""(string) 流ID """, dest='streamId',  required=True)),
            (['--start-time'], dict(help="""(string) 起始时间 """, dest='startTime',  required=False)),
            (['--end-time'], dict(help="""(string) 结束时间 """, dest='endTime',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取收流基础数据查询 ''',
        description='''
            获取收流基础数据查询。

            示例: jdc ams describe-streams-input  --stream-id xxx
        ''',
    )
    def describe_streams_input(self):
        client_factory = ClientFactory('ams')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ams.apis.DescribeStreamsInputRequest import DescribeStreamsInputRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeStreamsInputRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--p-id'], dict(help="""(string) PinId """, dest='pId',  required=True)),
            (['--ver'], dict(help="""(int) 版本 """, dest='ver', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 客户端鉴权查询 ''',
        description='''
            客户端鉴权查询。

            示例: jdc ams describe-authenticate  --p-id xxx
        ''',
    )
    def describe_authenticate(self):
        client_factory = ClientFactory('ams')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ams.apis.DescribeAuthenticateRequest import DescribeAuthenticateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAuthenticateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-streams-input','describe-authenticate',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('ams', self.app.pargs.api)
        skeleton.show()
