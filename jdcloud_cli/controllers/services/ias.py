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


class IasController(BaseController):
    class Meta:
        label = 'ias'
        help = 'JDCloud IAS'
        description = '''
        ias cli 子命令，京东云联合登陆。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/identity-authentication-service/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--pin'], dict(help="""(string) pin """, dest='pin',  required=True)),
            (['--app-name'], dict(help="""(string) appName """, dest='appName',  required=True)),
            (['--client-id'], dict(help="""(string) clientId """, dest='clientId',  required=True)),
            (['--multi-tenant'], dict(help="""(bool) multiTenant """, dest='multiTenant', type=bool, required=True)),
            (['--state'], dict(help="""(string) state """, dest='state',  required=True)),
            (['--scope'], dict(help="""(string) scope """, dest='scope',  required=True)),
            (['--start-time'], dict(help="""(int) startTime """, dest='startTime', type=int, required=True)),
            (['--end-time'], dict(help="""(int) endTime """, dest='endTime', type=int, required=True)),
            (['--account-type'], dict(help="""(string) accountType """, dest='accountType',  required=True)),
            (['--page-index'], dict(help="""(int) pageIndex """, dest='pageIndex', type=int, required=True)),
            (['--page-size'], dict(help="""(int) pageSize """, dest='pageSize', type=int, required=True)),
            (['--offset'], dict(help="""(int) offset """, dest='offset', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 运营后台查询app ''',
        description='''
            运营后台查询app。

            示例: jdc ias apps  --pin xxx --app-name xxx --client-id xxx --multi-tenant true --state xxx --scope xxx --start-time 5 --end-time 5 --account-type xxx --page-index 5 --page-size 5 --offset 5
        ''',
    )
    def apps(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.AppsRequest import AppsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AppsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--client-id'], dict(help="""(string) NA """, dest='clientId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 运营后台获取应用详情 ''',
        description='''
            运营后台获取应用详情。

            示例: jdc ias app-detail  --client-id xxx
        ''',
    )
    def app_detail(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.AppDetailRequest import AppDetailRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AppDetailRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 运营后台获取应用状态 ''',
        description='''
            运营后台获取应用状态。

            示例: jdc ias state 
        ''',
    )
    def state(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.StateRequest import StateRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = StateRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码，参考OpenAPI公共说明 """, dest='regionId',  required=False)),
            (['--client-name'], dict(help="""(string) 应用名 """, dest='clientName',  required=False)),
            (['--token-endpoint-auth-method'], dict(help="""(string) 客户端认证方式<br> - none：不设置客户端密码（不推荐）<br> - client_secret_post：客户端必须设置密码，且该密码需要在OAuth2 Token Endpoint提供于请求的body<br> - client_secret_basic：客户端必须设置密码，且该密码需要在OAuth2 Token Endpoint提供于请求的header<br> 支持以下值：<br> （1）none<br> （2）client_secret_post<br> （3）client_secret_basic """, dest='tokenEndpointAuthMethod',  required=False)),
            (['--grant-types'], dict(help="""(string) 支持的OAuth类型：<br> - authorization_code：OAuth2授权码模式<br> - implicit：OAuth2隐式授权模式<br> - refresh_token：启用刷新令牌 支持以下值：<br> （1）authorization_code<br> （2）authorization_code,refresh_token<br> （3）authorization_code,implicit<br> （4）authorization_code,implicit,refresh_token<br> （5）implicit<br> 注：如果grantTypes指定了refresh_token，应用将可以使用刷新令牌；如果在创建应用时未指定，则应用不能使用刷新令牌；任何时候应用都可以调用“更新应用”接口更改grantTypes设置 """, dest='grantTypes',  required=False)),
            (['--redirect-uris'], dict(help="""(string) 回调地址，最多4个，多个url之间用逗号,分隔，每个url长度不超过1000，url不支持#符号 """, dest='redirectUris',  required=False)),
            (['--client-uri'], dict(help="""(string) 应用介绍地址，url不支持#符号 """, dest='clientUri',  required=False)),
            (['--logo-uri'], dict(help="""(string) 应用logo地址，url不支持#符号 """, dest='logoUri',  required=False)),
            (['--tos-uri'], dict(help="""(string) 应用服务协议地址，url不支持#符号 """, dest='tosUri',  required=False)),
            (['--policy-uri'], dict(help="""(string) 应用隐私政策地址，url不支持#符号 """, dest='policyUri',  required=False)),
            (['--scope'], dict(help="""(string) OAuth scope范围，支持的值为：<br/> （1）openid：用OpenID Connect协议进行身份认证<br/> 指定scope为openid，并在Authorization Endpoint请求该scope，京东云将返回用户的OpenID令牌；如果在创建应用时未指明该值，则应用不能请求OpenID令牌；任何时候应用都可以调用“更新应用”更改该设置 """, dest='scope',  required=False)),
            (['--jwks-uri'], dict(help="""(string) JWKS地址，url不支持#符号<br/>jwksUri和jwks传一个即可 """, dest='jwksUri',  required=False)),
            (['--jwks'], dict(help="""(string) JWKS """, dest='jwks',  required=False)),
            (['--contacts'], dict(help="""(string) 应用联系信息 """, dest='contacts',  required=False)),
            (['--extension'], dict(help="""(string) 应用扩展信息 """, dest='extension',  required=False)),
            (['--access-token-validity-seconds'], dict(help="""(int) 访问令牌有效期，值的范围为 600 秒到 6x3600=21,600 秒，即10分钟-6小时 """, dest='accessTokenValiditySeconds', type=int, required=False)),
            (['--refresh-token-validity-seconds'], dict(help="""(int) 刷新令牌有效期，值的范围为 30x24x3600=2,592,000 秒到 365x24x3600=31,536,000 秒，即30天-365天<br/><br/> 注：当 GrantTypes 包含 refresh_token 时，refreshTokenValiditySeconds 为必传参数 """, dest='refreshTokenValiditySeconds', type=int, required=False)),
            (['--multi-tenant'], dict(help="""(bool) 是否为多租户应用<br/> "false"：该应用仅支持当前创建应用的租户访问，其他京东云租户无法访问<br/>        "true"：该应用支持其他京东云租户访问，但当前创建应用的租户不能访问 """, dest='multiTenant', type=bool, required=False)),
            (['--secret'], dict(help="""(string) 应用的密码，支持8-255位长度的ASCII可打印字符，建议使用足够复杂的密码策略<br/><br/>        注：当TokenEndpointAuthMethod不等于none时，secret为必传参数；反之，当指定了secret时，TokenEndpointAuthMethod不能等于none<br/>京东云将不可逆加密secret，因此您无法再次从京东云查看该密码，但您可以随时通过更新应用重新设置secret """, dest='secret',  required=False)),
            (['--user-type'], dict(help="""(string) 能访问应用的账号类型，支持以下值：<br/> （1）root：支持主账号访问，子用户无法访问<br/> （2）sub：子用户账号，使用主账号不能访问<br/><br/> 注：multiTenant和userType的组合指定了应用的用户人群，典型的应用场景如：<br/> （1）应用向当前租户下的子用户开放（2）应用向京东云其他租户主账号开放 """, dest='userType',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建应用 ''',
        description='''
            创建应用。

            示例: jdc ias create-app 
        ''',
    )
    def create_app(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.CreateAppRequest import CreateAppRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateAppRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码，参考OpenAPI公共说明 """, dest='regionId',  required=False)),
            (['--client-id'], dict(help="""(string) 应用ID，应用创建时由京东云分配的16位数字ID """, dest='clientId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取应用 ''',
        description='''
            获取应用。

            示例: jdc ias get-app  --client-id xxx
        ''',
    )
    def get_app(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.GetAppRequest import GetAppRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetAppRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码，参考OpenAPI公共说明 """, dest='regionId',  required=False)),
            (['--client-id'], dict(help="""(string) 应用ID，应用创建时由京东云分配的16位数字ID """, dest='clientId',  required=True)),
            (['--client-name'], dict(help="""(string) 应用名 """, dest='clientName',  required=False)),
            (['--token-endpoint-auth-method'], dict(help="""(string) 客户端认证方式：<br/> none：不设置客户端密码（不推荐）<br/> client_secret_post：客户端必须设置密码，且该密码需要在OAuth2 Token Endpoint提供于请求的body<br/> client_secret_basic：客户端必须设置密码，且该密码需要在OAuth2 Token Endpoint提供于请求的header<br/><br/> 支持以下值：<br/> （1）none<br/> （2）client_secret_post<br/> （3）client_secret_basic """, dest='tokenEndpointAuthMethod',  required=False)),
            (['--grant-types'], dict(help="""(string) 支持的OAuth类型：<br/> authorization_code：OAuth2授权码模式<br/> implicit：OAuth2隐式授权模式<br/> refresh_token：启用刷新令牌<br/><br/> 支持以下值：<br/> （1）authorization_code<br/> （2）authorization_code,refresh_token<br/> （3）authorization_code,implicit<br/> （4）authorization_code,implicit,refresh_token<br/> （5）implicit<br/><br/>        注：如果grantTypes指定了refresh_token，应用将可以使用刷新令牌；如果在创建应用时未指定，则应用不能使用刷新令牌；任何时候应用都可以调用“更新应用”接口更改grantTypes设置 """, dest='grantTypes',  required=False)),
            (['--redirect-uris'], dict(help="""(string) 回调地址，最多4个，多个url之间用逗号,分隔，每个url长度不超过1000，url不支持#符号 """, dest='redirectUris',  required=False)),
            (['--client-uri'], dict(help="""(string) 应用介绍地址，url不支持#符号 """, dest='clientUri',  required=False)),
            (['--logo-uri'], dict(help="""(string) 应用logo地址，url不支持#符号 """, dest='logoUri',  required=False)),
            (['--tos-uri'], dict(help="""(string) 应用服务协议地址，url不支持#符号 """, dest='tosUri',  required=False)),
            (['--policy-uri'], dict(help="""(string) 应用隐私政策地址，url不支持#符号 """, dest='policyUri',  required=False)),
            (['--scope'], dict(help="""(string) OAuth scope范围，支持的值为：<br/> （1）openid：用OpenID Connect协议进行身份认证<br/> 指定scope为openid，并在Authorization Endpoint请求该scope，京东云将返回用户的OpenID令牌；如果在创建应用时未指明该值，则应用不能请求OpenID令牌；任何时候应用都可以调用“更新应用”更改该设置 """, dest='scope',  required=False)),
            (['--jwks-uri'], dict(help="""(string) JWKS地址，url不支持#符号<br/> jwksUri和jwks传一个即可 """, dest='jwksUri',  required=False)),
            (['--jwks'], dict(help="""(string) JWKS """, dest='jwks',  required=False)),
            (['--contacts'], dict(help="""(string) 应用联系信息 """, dest='contacts',  required=False)),
            (['--extension'], dict(help="""(string) 应用扩展信息 """, dest='extension',  required=False)),
            (['--access-token-validity-seconds'], dict(help="""(int) 访问令牌有效期，值的范围为 600 秒到 6x3600=21,600 秒，即10分钟-6小时 """, dest='accessTokenValiditySeconds', type=int, required=False)),
            (['--refresh-token-validity-seconds'], dict(help="""(int) 刷新令牌有效期，值的范围为 30x24x3600=2,592,000 秒到 365x24x3600=31,536,000 秒，即30天-365天<br/><br/> 注：当 GrantTypes 包含 refresh_token 时，refreshTokenValiditySeconds 为必传参数 """, dest='refreshTokenValiditySeconds', type=int, required=False)),
            (['--multi-tenant'], dict(help="""(bool) 是否为多租户应用<br/> "false"：该应用仅支持当前创建应用的租户访问，其他京东云租户无法访问<br/>        "true"：该应用支持其他京东云租户访问，但当前创建应用的租户不能访问 """, dest='multiTenant', type=bool, required=False)),
            (['--secret'], dict(help="""(string) 应用的密码，支持8-255位长度的ASCII可打印字符，建议使用足够复杂的密码策略<br/><br/> 注：当TokenEndpointAuthMethod不等于none时，secret为必传参数；反之，当指定了secret时，TokenEndpointAuthMethod不能等于none<br/> 京东云将不可逆加密secret，因此您无法再次从京东云查看该密码，但您可以随时通过更新应用重新设置secret """, dest='secret',  required=False)),
            (['--user-type'], dict(help="""(string) 能访问应用的账号类型，支持以下值：<br/> （1）root：支持主账号访问，子用户无法访问<br/> （2）sub：子用户账号，使用主账号不能访问<br/><br/> 注：multiTenant和userType的组合指定了应用的用户人群，典型的应用场景如：<br/> （1）应用向当前租户下的子用户开放（2）应用向京东云其他租户主账号开放 """, dest='userType',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 更新应用（只传需要变更的参数，不传的参数不会更新） ''',
        description='''
            更新应用（只传需要变更的参数，不传的参数不会更新）。

            示例: jdc ias update-app  --client-id xxx
        ''',
    )
    def update_app(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.UpdateAppRequest import UpdateAppRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateAppRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码，参考OpenAPI公共说明 """, dest='regionId',  required=False)),
            (['--client-id'], dict(help="""(string) 应用ID，应用创建时由京东云分配的16位数字ID """, dest='clientId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除应用 ''',
        description='''
            删除应用。

            示例: jdc ias delete-app  --client-id xxx
        ''',
    )
    def delete_app(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.DeleteAppRequest import DeleteAppRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteAppRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域编码，参考OpenAPI公共说明 """, dest='regionId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 获取账户下所有应用 ''',
        description='''
            获取账户下所有应用。

            示例: jdc ias get-apps 
        ''',
    )
    def get_apps(self):
        client_factory = ClientFactory('ias')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.ias.apis.GetAppsRequest import GetAppsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetAppsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['apps','app-detail','state','create-app','get-app','update-app','delete-app','get-apps',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('ias', self.app.pargs.api)
        skeleton.show()
