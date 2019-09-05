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


class YundingdatapushController(BaseController):
    class Meta:
        label = 'yundingdatapush'
        help = '云鼎2.0数据推送 openApi'
        description = '''
        yundingdatapush cli 子命令，云鼎2.0数据推送 openApi 相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--appkey'], dict(help="""(string) appkey """, dest='appkey',  required=True)),
            (['--page-number'], dict(help="""(int) 页码 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 页大小 """, dest='pageSize', type=int, required=False)),
            (['--yd-rds-instance-id'], dict(help="""(string) 云鼎数据库实例ID """, dest='ydRdsInstanceId',  required=False)),
            (['--rds-instance-name'], dict(help="""(string) 数据库实例名称 """, dest='rdsInstanceName',  required=False)),
            (['--vender-id'], dict(help="""(string) 商家ID """, dest='venderId',  required=False)),
            (['--vender-name'], dict(help="""(string) 商家店铺名称 """, dest='venderName',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询已经开通的用户 ''',
        description='''
            查询已经开通的用户。

            示例: jdc yundingdatapush describe-datapush-venders  --appkey xxx
        ''',
    )
    def describe_datapush_venders(self):
        client_factory = ClientFactory('yundingdatapush')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.yundingdatapush.apis.DescribeDatapushVendersRequest import DescribeDatapushVendersRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeDatapushVendersRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--datapush-vender'], dict(help="""(vender) 添加/删除数据推送用户对象;  """, dest='datapushVender',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加数据推送用户 ''',
        description='''
            添加数据推送用户。

            示例: jdc yundingdatapush add-datapush-vender  --datapush-vender '{"":""}'
        ''',
    )
    def add_datapush_vender(self):
        client_factory = ClientFactory('yundingdatapush')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.yundingdatapush.apis.AddDatapushVenderRequest import AddDatapushVenderRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AddDatapushVenderRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--appkey'], dict(help="""(string) appkey """, dest='appkey',  required=True)),
            (['--yd-rds-instance-id'], dict(help="""(string) 云鼎数据库实例ID """, dest='ydRdsInstanceId',  required=True)),
            (['--vender-id'], dict(help="""(string) 商家ID """, dest='venderId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除数据推送用户 ''',
        description='''
            删除数据推送用户。

            示例: jdc yundingdatapush delete-datapush-vender  --appkey xxx --yd-rds-instance-id xxx --vender-id xxx
        ''',
    )
    def delete_datapush_vender(self):
        client_factory = ClientFactory('yundingdatapush')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.yundingdatapush.apis.DeleteDatapushVenderRequest import DeleteDatapushVenderRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteDatapushVenderRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--appkey'], dict(help="""(string) appkey """, dest='appkey',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询开通数据推送的数据库实例 ''',
        description='''
            查询开通数据推送的数据库实例。

            示例: jdc yundingdatapush describe-rds-instances  --appkey xxx
        ''',
    )
    def describe_rds_instances(self):
        client_factory = ClientFactory('yundingdatapush')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.yundingdatapush.apis.DescribeRdsInstancesRequest import DescribeRdsInstancesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeRdsInstancesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-datapush-venders','add-datapush-vender','delete-datapush-vender','describe-rds-instances',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('yundingdatapush', self.app.pargs.api)
        skeleton.show()
