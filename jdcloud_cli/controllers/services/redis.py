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
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from argparse import RawTextHelpFormatter
from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class RedisController(BaseController):
    class Meta:
        label = 'redis'
        help = '使用该子命令操作redis相关资源'
        description = '''
        redis cli 子命令，可以使用该子命令操作redis相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/384/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', required=False)),
            (['--filters'], dict(help="""(array: filter) cacheInstanceId -实例Id，精确匹配，支持多个; cacheInstanceName - 实例名称，模糊匹配，支持单个; cacheInstanceStatus - redis状态，精确匹配，支持多个(running：运行，error：错误，creating：创建中，changing：变配中，deleting：删除中);  """, dest='filters', required=False)),
            (['--sorts'], dict(help="""(array: sort) createTime - 创建时间(asc：正序，desc：倒序);  """, dest='sorts', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询缓存Redis实例列表 ''',
        description='''
            查询缓存Redis实例列表。

            示例: jdc redis describe-cache-instances 
        ''',
    )
    def describe_cache_instances(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.DescribeCacheInstancesRequest import DescribeCacheInstancesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeCacheInstancesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--cache-instance'], dict(help="""(cacheInstanceSpec) NA """, dest='cacheInstance', required=True)),
            (['--charge'], dict(help="""(chargeSpec) NA """, dest='charge', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建一个指定配置的缓存Redis实例 ''',
        description='''
            创建一个指定配置的缓存Redis实例。

            示例: jdc redis create-cache-instance  --cache-instance {"":""}
        ''',
    )
    def create_cache_instance(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.CreateCacheInstanceRequest import CreateCacheInstanceRequest
            params_dict = collect_user_args(self.app)
            req = CreateCacheInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID """, dest='cacheInstanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询缓存Redis实例详情 ''',
        description='''
            查询缓存Redis实例详情。

            示例: jdc redis describe-cache-instance  --cache-instance-id xxx
        ''',
    )
    def describe_cache_instance(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.DescribeCacheInstanceRequest import DescribeCacheInstanceRequest
            params_dict = collect_user_args(self.app)
            req = DescribeCacheInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID """, dest='cacheInstanceId', required=True)),
            (['--cache-instance-name'], dict(help="""(string) 缓存Redis实例资源名称 """, dest='cacheInstanceName', required=False)),
            (['--cache-instance-description'], dict(help="""(string) 缓存Redis实例资源描述 """, dest='cacheInstanceDescription', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改缓存Redis实例的资源名称、描述，二者至少选一 ''',
        description='''
            修改缓存Redis实例的资源名称、描述，二者至少选一。

            示例: jdc redis modify-cache-instance-attribute  --cache-instance-id xxx
        ''',
    )
    def modify_cache_instance_attribute(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.ModifyCacheInstanceAttributeRequest import ModifyCacheInstanceAttributeRequest
            params_dict = collect_user_args(self.app)
            req = ModifyCacheInstanceAttributeRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID """, dest='cacheInstanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除单个缓存Redis实例 ''',
        description='''
            删除单个缓存Redis实例。

            示例: jdc redis delete-cache-instance  --cache-instance-id xxx
        ''',
    )
    def delete_cache_instance(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.DeleteCacheInstanceRequest import DeleteCacheInstanceRequest
            params_dict = collect_user_args(self.app)
            req = DeleteCacheInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID """, dest='cacheInstanceId', required=True)),
            (['--cache-instance-class'], dict(help="""(string) 变更后的缓存Redis<a href="https://www.jdcloud.com/help/detail/411/isCatalog/1">实例规格代码</a> """, dest='cacheInstanceClass', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 变更缓存Redis实例配置 ''',
        description='''
            变更缓存Redis实例配置。

            示例: jdc redis modify-cache-instance-class  --cache-instance-id xxx --cache-instance-class xxx
        ''',
    )
    def modify_cache_instance_class(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.ModifyCacheInstanceClassRequest import ModifyCacheInstanceClassRequest
            params_dict = collect_user_args(self.app)
            req = ModifyCacheInstanceClassRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID """, dest='cacheInstanceId', required=True)),
            (['--password'], dict(help="""(string) 密码，必须包含且只支持字母及数字，不少于8字符不超过16字符 """, dest='password', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 重置缓存Redis实例密码 ''',
        description='''
            重置缓存Redis实例密码。

            示例: jdc redis reset-cache-instance-password  --cache-instance-id xxx --password xxx
        ''',
    )
    def reset_cache_instance_password(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.ResetCacheInstancePasswordRequest import ResetCacheInstancePasswordRequest
            params_dict = collect_user_args(self.app)
            req = ResetCacheInstancePasswordRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某区域下的实例规格列表 ''',
        description='''
            查询某区域下的实例规格列表。

            示例: jdc redis describe-instance-class 
        ''',
    )
    def describe_instance_class(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.DescribeInstanceClassRequest import DescribeInstanceClassRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstanceClassRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前缓存Redis有华北、华南、华东区域，对应Region ID为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询账户配额信息 ''',
        description='''
            查询账户配额信息。

            示例: jdc redis describe-user-quota 
        ''',
    )
    def describe_user_quota(self):
        client_factory = ClientFactory('redis')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.redis.apis.DescribeUserQuotaRequest import DescribeUserQuotaRequest
            params_dict = collect_user_args(self.app)
            req = DescribeUserQuotaRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-cache-instances','create-cache-instance','describe-cache-instance','modify-cache-instance-attribute','delete-cache-instance','modify-cache-instance-class','reset-cache-instance-password','describe-instance-class','describe-user-quota',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('redis', self.app.pargs.api)
        skeleton.show()
