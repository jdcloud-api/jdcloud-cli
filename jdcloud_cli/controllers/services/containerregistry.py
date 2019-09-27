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


class ContainerregistryController(BaseController):
    class Meta:
        label = 'containerregistry'
        help = '容器镜像仓库'
        description = '''
        containerregistry cli 子命令，容器镜像仓库服务。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/containerregistry/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--expired-after-hours'], dict(help="""(int) issue新token的过期时间, 可选参数为新生成令牌的过期时间，最大值为24小时，最小值为1小时，为空则默认为12小时过期时间。;  """, dest='expiredAfterHours', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' <p>申请12小时有效期的令牌。 使用<code>docker</code> CLI push和pull镜像。</p>; <p><code>authorizationToken</code>为每个registry返回一个base64编码的字符串，解码后<code>docker login</code>命令; 可完成指定registry的鉴权。JCR CLI提供<code>jcr get-login</code>进行认证处理。</p>;  ''',
        description='''
            <p>申请12小时有效期的令牌。 使用<code>docker</code> CLI push和pull镜像。</p>; <p><code>authorizationToken</code>为每个registry返回一个base64编码的字符串，解码后<code>docker login</code>命令; 可完成指定registry的鉴权。JCR CLI提供<code>jcr get-login</code>进行认证处理。</p>; 。

            示例: jdc containerregistry get-authorization-token  --registry-name xxx
        ''',
    )
    def get_authorization_token(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.GetAuthorizationTokenRequest import GetAuthorizationTokenRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetAuthorizationTokenRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--filters'], dict(help="""(array: filter) token - 令牌 ID，支持多个;  """, dest='filters',  required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' <p>批量查询令牌。</p> ; <p>暂时不支持分页和过滤条件。</p>;  ''',
        description='''
            <p>批量查询令牌。</p> ; <p>暂时不支持分页和过滤条件。</p>; 。

            示例: jdc containerregistry describe-authorization-tokens  --registry-name xxx
        ''',
    )
    def describe_authorization_tokens(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DescribeAuthorizationTokensRequest import DescribeAuthorizationTokensRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAuthorizationTokensRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域 ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--authorization-token'], dict(help="""(string) 准备释放的 token ID，功能为指定token释放。 """, dest='authorizationToken',  required=False)),
            (['--force-all'], dict(help="""(bool) true 表示强制删除用户当前registry下所有有效token的标志；false 表示删除所有有效token。 """, dest='forceAll',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 释放用户 registry 的 token。;  ''',
        description='''
            释放用户 registry 的 token。; 。

            示例: jdc containerregistry release-authorization-token  --registry-name xxx
        ''',
    )
    def release_authorization_token(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.ReleaseAuthorizationTokenRequest import ReleaseAuthorizationTokenRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ReleaseAuthorizationTokenRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--filters'], dict(help="""(array: filter) registryName - 镜像仓储名称 ; repositoryName - 镜像库名称 ; imageDigest - 镜像哈希值 ; imageTag - 镜像标签 ; tagStatus - 打标TAGGED或没打标UNTAGGED ;  """, dest='filters',  required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 返回指定repository中images的元数据，包括image size, image tags和creation date。;  ''',
        description='''
            返回指定repository中images的元数据，包括image size, image tags和creation date。; 。

            示例: jdc containerregistry describe-images 
        ''',
    )
    def describe_images(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DescribeImagesRequest import DescribeImagesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeImagesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--repository-name'], dict(help="""(string) 镜像仓库表名称 """, dest='repositoryName',  required=True)),
            (['--image-digest'], dict(help="""(string) sha256哈希，image manifest的digest. """, dest='imageDigest',  required=False)),
            (['--image-tag'], dict(help="""(string) image使用的tag """, dest='imageTag',  required=False)),
            (['--image-tag-status'], dict(help="""(string) 枚举中的一个值，如 tagged 和 untagged. """, dest='imageTagStatus',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除镜像; imageDigest imageTag imageTagStatus 三者只能且必须传一个。; 可根据Tag状态删除Image，例如删除所有tagged的镜像。; digest和tag唯一表征单个镜像，其中imageDigest为sha256哈希，image manifest的digest。; 例如 sha256:examplee6d1e504117a17000003d3753086354a38375961f2e665416ef4b1b2f；image使用的tag, 如  "precise" ;  [MFA enabled] ''',
        description='''
            删除镜像; imageDigest imageTag imageTagStatus 三者只能且必须传一个。; 可根据Tag状态删除Image，例如删除所有tagged的镜像。; digest和tag唯一表征单个镜像，其中imageDigest为sha256哈希，image manifest的digest。; 例如 sha256:examplee6d1e504117a17000003d3753086354a38375961f2e665416ef4b1b2f；image使用的tag, 如  "precise" ;  [MFA enabled]。

            示例: jdc containerregistry delete-image  --registry-name xxx --repository-name xxx
        ''',
    )
    def delete_image(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DeleteImageRequest import DeleteImageRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteImageRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--filters'], dict(help="""(array: filter) resourceTypes - 资源类型，暂时只支持 [registry, repository]，支持同时查询两种配额。;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询配额 ''',
        description='''
            查询配额。

            示例: jdc containerregistry describe-quotas 
        ''',
    )
    def describe_quotas(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DescribeQuotasRequest import DescribeQuotasRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeQuotasRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 批量查询指定用户下所有 registry 详情。; 暂不支持 filter.;  ''',
        description='''
            批量查询指定用户下所有 registry 详情。; 暂不支持 filter.; 。

            示例: jdc containerregistry describe-registries 
        ''',
    )
    def describe_registries(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DescribeRegistriesRequest import DescribeRegistriesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeRegistriesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 用户定义的registry名称。<br> DNS兼容registry名称规则如下：;  <br> 不可为空，且不能超过32字符 <br> 以小写字母开始和结尾，支持使用小写字母、数字、中划线(-);  """, dest='registryName',  required=True)),
            (['--description'], dict(help="""(string) 注册表描述，<a href="https://www.jdcloud.com/help/detail/3870/isCatalog/1">参考公共参数规范</a>。;  """, dest='description',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 通过参数创建注册表。;  ''',
        description='''
            通过参数创建注册表。; 。

            示例: jdc containerregistry create-registry  --registry-name xxx
        ''',
    )
    def create_registry(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.CreateRegistryRequest import CreateRegistryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateRegistryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询指定用户下某个 registry 详情。;  ''',
        description='''
            查询指定用户下某个 registry 详情。; 。

            示例: jdc containerregistry describe-registry  --registry-name xxx
        ''',
    )
    def describe_registry(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DescribeRegistryRequest import DescribeRegistryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeRegistryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除指定用户下某个 registry.;  [MFA enabled] ''',
        description='''
            删除指定用户下某个 registry.;  [MFA enabled]。

            示例: jdc containerregistry delete-registry  --registry-name xxx
        ''',
    )
    def delete_registry(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DeleteRegistryRequest import DeleteRegistryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteRegistryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 待验证的注册表名。 """, dest='registryName',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询指定注册表名称是否已经存在以及是否符合命名规范。;  ''',
        description='''
            查询指定注册表名称是否已经存在以及是否符合命名规范。; 。

            示例: jdc containerregistry check-registry-name  --registry-name xxx
        ''',
    )
    def check_registry_name(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.CheckRegistryNameRequest import CheckRegistryNameRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CheckRegistryNameRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--repository-name'], dict(help="""(string) 镜像仓库名称。; 可以专有模式如默认命名空间nginx-web-app；或者和命名空间一起将多个仓库聚集在一起如 project-a/nginx-web-app。;  """, dest='repositoryName',  required=True)),
            (['--description'], dict(help="""(string) 注册表描述，<a href="https://www.jdcloud.com/help/detail/3870/isCatalog/1">参考公共参数规范</a>。;  """, dest='description',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 通过参数创建镜像仓库。; 仓库名称可以分解为多个路径名，每个名称必须至少包含一个小写字母数字，考虑URL规范。; 支持包含段划线或者下划线进行分割，但不允许点'.'，多个路径名之间通过("/")连接，总长度不超过256个字符，当前只支持二级目录。;  ''',
        description='''
            通过参数创建镜像仓库。; 仓库名称可以分解为多个路径名，每个名称必须至少包含一个小写字母数字，考虑URL规范。; 支持包含段划线或者下划线进行分割，但不允许点'.'，多个路径名之间通过("/")连接，总长度不超过256个字符，当前只支持二级目录。; 。

            示例: jdc containerregistry create-repository  --registry-name xxx --repository-name xxx
        ''',
    )
    def create_repository(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.CreateRepositoryRequest import CreateRepositoryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateRepositoryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--filters'], dict(help="""(array: filter) name - 仓库名称，模糊匹配，支持单个;  """, dest='filters',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名 """, dest='registryName',  required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 描述用户指定 registry 下的 repository.;  ''',
        description='''
            描述用户指定 registry 下的 repository.; 。

            示例: jdc containerregistry describe-repositories 
        ''',
    )
    def describe_repositories(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DescribeRepositoriesRequest import DescribeRepositoriesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeRepositoriesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名称 """, dest='registryName',  required=True)),
            (['--repository-name'], dict(help="""(string) 镜像仓库名称 """, dest='repositoryName',  required=True)),
            (['--force'], dict(help="""(bool) 是否强制删除有镜像的镜像仓库 """, dest='force',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除指定用户下某个镜像仓库.;  [MFA enabled] ''',
        description='''
            删除指定用户下某个镜像仓库.;  [MFA enabled]。

            示例: jdc containerregistry delete-repository  --registry-name xxx --repository-name xxx
        ''',
    )
    def delete_repository(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.DeleteRepositoryRequest import DeleteRepositoryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteRepositoryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--registry-name'], dict(help="""(string) 注册表名。 """, dest='registryName',  required=True)),
            (['--repository-name'], dict(help="""(string) 待验证的镜像仓库名。 """, dest='repositoryName',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询指定镜像仓库名称是否已经存在以及是否符合命名规范。;  ''',
        description='''
            查询指定镜像仓库名称是否已经存在以及是否符合命名规范。; 。

            示例: jdc containerregistry check-repository-name  --registry-name xxx --repository-name xxx
        ''',
    )
    def check_repository_name(self):
        client_factory = ClientFactory('containerregistry')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.containerregistry.apis.CheckRepositoryNameRequest import CheckRepositoryNameRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CheckRepositoryNameRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['get-authorization-token','describe-authorization-tokens','release-authorization-token','describe-images','delete-image','describe-quotas','describe-registries','create-registry','describe-registry','delete-registry','check-registry-name','create-repository','describe-repositories','delete-repository','check-repository-name',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('containerregistry', self.app.pargs.api)
        skeleton.show()
