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


class SslController(BaseController):
    class Meta:
        label = 'ssl'
        help = 'JDCLOUD SSL数字证书管理 API'
        description = '''
        ssl cli 子命令，提供SSL数字证书，证书申购记录管理相关信息接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 第几页，从1开始计数 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 每页显示的数目 """, dest='pageSize', type=int, required=False)),
            (['--domain-name'], dict(help="""(string) 域名，支持按照域名检索证书 """, dest='domainName',  required=False)),
            (['--cert-ids'], dict(help="""(string) 证书id/别名 """, dest='certIds',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看证书列表 ''',
        description='''
            查看证书列表。

            示例: jdc ssl describe-certs 
        ''',
    )
    def describe_certs(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.DescribeCertsRequest import DescribeCertsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeCertsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--cert-id'], dict(help="""(string) 证书 Id """, dest='certId',  required=True)),
            (['--page-number'], dict(help="""(int) 第几页，从1开始计数 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 每页显示的数目 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看证书详情 ''',
        description='''
            查看证书详情。

            示例: jdc ssl describe-cert  --cert-id xxx
        ''',
    )
    def describe_cert(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.DescribeCertRequest import DescribeCertRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeCertRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--cert-id'], dict(help="""(string) 证书 Id """, dest='certId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除证书 [MFA enabled] ''',
        description='''
            删除证书 [MFA enabled]。

            示例: jdc ssl delete-certs  --cert-id xxx
        ''',
    )
    def delete_certs(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.DeleteCertsRequest import DeleteCertsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteCertsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--cert-name'], dict(help="""(string) 证书名称 """, dest='certName',  required=True)),
            (['--key-file'], dict(help="""(string) 私钥 """, dest='keyFile',  required=True)),
            (['--cert-file'], dict(help="""(string) 证书 """, dest='certFile',  required=True)),
            (['--alias-name'], dict(help="""(string) 证书别名 """, dest='aliasName',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 上传证书 ''',
        description='''
            上传证书。

            示例: jdc ssl upload-cert  --cert-name xxx --key-file xxx --cert-file xxx
        ''',
    )
    def upload_cert(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.UploadCertRequest import UploadCertRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UploadCertRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--cert-id'], dict(help="""(string) 证书Id,以逗号分隔多个Id """, dest='certId',  required=True)),
            (['--server-type'], dict(help="""(string) 证书应用的服务器类型(Nginx Apache Tomcat IIS Other) """, dest='serverType',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 下载证书 [MFA enabled] ''',
        description='''
            下载证书 [MFA enabled]。

            示例: jdc ssl download-cert  --cert-id xxx --server-type xxx
        ''',
    )
    def download_cert(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.DownloadCertRequest import DownloadCertRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DownloadCertRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--cert-id'], dict(help="""(string) 证书Id """, dest='certId',  required=True)),
            (['--cert-name'], dict(help="""(string) 证书名称 """, dest='certName',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改证书名称 ''',
        description='''
            修改证书名称。

            示例: jdc ssl update-cert-name  --cert-id xxx --cert-name xxx
        ''',
    )
    def update_cert_name(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.UpdateCertNameRequest import UpdateCertNameRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateCertNameRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--cert-id'], dict(help="""(string) 证书ID """, dest='certId',  required=True)),
            (['--key-file'], dict(help="""(string) 私钥 """, dest='keyFile',  required=True)),
            (['--cert-file'], dict(help="""(string) 证书 """, dest='certFile',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 更新证书 [MFA enabled] ''',
        description='''
            更新证书 [MFA enabled]。

            示例: jdc ssl update-cert  --cert-id xxx --key-file xxx --cert-file xxx
        ''',
    )
    def update_cert(self):
        client_factory = ClientFactory('ssl')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ssl.apis.UpdateCertRequest import UpdateCertRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateCertRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-certs','describe-cert','delete-certs','upload-cert','download-cert','update-cert-name','update-cert',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('ssl', self.app.pargs.api)
        skeleton.show()
