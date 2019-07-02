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


class RedisController(BaseController):
    class Meta:
        label = 'redis'
        help = 'JDCloud Redis API'
        description = '''
        redis cli 子命令，京东云缓存Redis相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/jcs-for-redis/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--page-number'], dict(help="""(int) 页码：取值范围[1,∞)，默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小：取值范围[10, 100]，默认为10 """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) 过滤属性：; cacheInstanceId - 实例Id，精确匹配，可选择多个; cacheInstanceName - 实例名称，模糊匹配; cacheInstanceStatus - 实例状态，精确匹配，可选择多个(running：运行中，error：错误，creating：创建中，changing：变配中，configuring：参数修改中，restoring：备份恢复中，deleting：删除中); redisVersion - redis引擎版本，精确匹配，可选择2.8和4.0; instanceType - 实例类型，精确匹配（redis表示主从版，redis_cluster表示集群版）; chargeMode - 计费类型，精确匹配（prepaid_by_duration表示包年包月预付费，postpaid_by_duration表示按配置后付费）;  """, dest='filters',  required=False)),
            (['--sorts'], dict(help="""(array: sort) 排序属性：; createTime - 按创建时间排序(asc表示按时间正序，desc表示按时间倒序);  """, dest='sorts',  required=False)),
            (['--tag-filters'], dict(help="""(array: tagFilter) 标签的过滤条件 """, dest='tagFilters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询缓存Redis实例列表，可分页、可排序、可搜索、可过滤 ''',
        description='''
            查询缓存Redis实例列表，可分页、可排序、可搜索、可过滤。

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
            headers = collect_user_headers(self.app)
            req = DescribeCacheInstancesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--cache-instance'], dict(help="""(cacheInstanceSpec) 创建实例时输入的信息 """, dest='cacheInstance',  required=True)),
            (['--charge'], dict(help="""(chargeSpec) 该实例规格的计费信息 """, dest='charge',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建一个指定配置的缓存Redis实例：可选择主从版或集群版，每种类型又分为多种规格（按CPU核数、内存容量、磁盘容量、带宽等划分），具体可参考产品规格代码，https://docs.jdcloud.com/cn/jcs-for-redis/specifications;  ''',
        description='''
            创建一个指定配置的缓存Redis实例：可选择主从版或集群版，每种类型又分为多种规格（按CPU核数、内存容量、磁盘容量、带宽等划分），具体可参考产品规格代码，https://docs.jdcloud.com/cn/jcs-for-redis/specifications; 。

            示例: jdc redis create-cache-instance  --cache-instance '{"":""}'
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
            headers = collect_user_headers(self.app)
            req = CreateCacheInstanceRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID，是访问实例的唯一标识 """, dest='cacheInstanceId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询缓存Redis实例的详细信息 ''',
        description='''
            查询缓存Redis实例的详细信息。

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
            headers = collect_user_headers(self.app)
            req = DescribeCacheInstanceRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID，是访问实例的唯一标识 """, dest='cacheInstanceId',  required=True)),
            (['--cache-instance-name'], dict(help="""(string) 实例的名称，名称只支持数字、字母、英文下划线、中文，且不少于2字符不超过32字符 """, dest='cacheInstanceName',  required=False)),
            (['--cache-instance-description'], dict(help="""(string) 实例的描述，不能超过256个字符 """, dest='cacheInstanceDescription',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改缓存Redis实例的资源名称或描述，二者至少选一 ''',
        description='''
            修改缓存Redis实例的资源名称或描述，二者至少选一。

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
            headers = collect_user_headers(self.app)
            req = ModifyCacheInstanceAttributeRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID，是访问实例的唯一标识 """, dest='cacheInstanceId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除按配置计费、或包年包月已到期的缓存Redis实例，包年包月未到期不可删除。; 只有处于运行running或者错误error状态才可以删除，其余状态不可以删除。; 白名单用户不能删除包年包月已到期的缓存Redis实例。;  ''',
        description='''
            删除按配置计费、或包年包月已到期的缓存Redis实例，包年包月未到期不可删除。; 只有处于运行running或者错误error状态才可以删除，其余状态不可以删除。; 白名单用户不能删除包年包月已到期的缓存Redis实例。; 。

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
            headers = collect_user_headers(self.app)
            req = DeleteCacheInstanceRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID，是访问实例的唯一标识 """, dest='cacheInstanceId',  required=True)),
            (['--cache-instance-class'], dict(help="""(string) 变更后的实例规格 """, dest='cacheInstanceClass',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 变更缓存Redis实例规格（变配），只能变更运行状态的实例规格，变更的规格不能与之前的相同。; 预付费用户，从集群版变配到主从版，新规格的内存大小要大于老规格的内存大小，从主从版到集群版，新规格的内存大小要不小于老规格的内存大小。;  ''',
        description='''
            变更缓存Redis实例规格（变配），只能变更运行状态的实例规格，变更的规格不能与之前的相同。; 预付费用户，从集群版变配到主从版，新规格的内存大小要大于老规格的内存大小，从主从版到集群版，新规格的内存大小要不小于老规格的内存大小。; 。

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
            headers = collect_user_headers(self.app)
            req = ModifyCacheInstanceClassRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--cache-instance-id'], dict(help="""(string) 缓存Redis实例ID，是访问实例的唯一标识 """, dest='cacheInstanceId',  required=True)),
            (['--password'], dict(help="""(string) 密码，为空即为免密，不少于8字符不超过16字符 """, dest='password',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 重置缓存Redis实例的密码，可为空 ''',
        description='''
            重置缓存Redis实例的密码，可为空。

            示例: jdc redis reset-cache-instance-password  --cache-instance-id xxx
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
            headers = collect_user_headers(self.app)
            req = ResetCacheInstancePasswordRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--redis-version'], dict(help="""(string) 缓存Redis的版本号：目前有2.8和4.0，默认为2.8 """, dest='redisVersion',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某区域下的缓存Redis实例规格列表 ''',
        description='''
            查询某区域下的缓存Redis实例规格列表。

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
            headers = collect_user_headers(self.app)
            req = DescribeInstanceClassRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2 """, dest='regionId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询账户的缓存Redis配额信息 ''',
        description='''
            查询账户的缓存Redis配额信息。

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
            headers = collect_user_headers(self.app)
            req = DescribeUserQuotaRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

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
