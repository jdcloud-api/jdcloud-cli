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
from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args, collect_user_headers
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class DiskController(BaseController):
    class Meta:
        label = 'disk'
        help = '使用该子命令操作disk相关资源'
        description = '''
        disk cli 子命令，可以使用该子命令操作disk相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/377/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1, 取值范围：[1,∞) """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20，取值范围：[10,100] """, dest='pageSize', required=False)),
            (['--tags'], dict(help="""(array: tagFilter) Tag筛选条件 """, dest='tags', required=False)),
            (['--filters'], dict(help="""(array: filter) diskId - 云硬盘ID，精确匹配，支持多个; diskType - 云硬盘类型，精确匹配，支持多个，取值为 ssd 或 premium-hdd; instanceId - 云硬盘所挂载主机的ID，精确匹配，支持多个; instanceType - 云硬盘所挂载主机的类型，精确匹配，支持多个; status - 可用区，精确匹配，支持多个; az - 云硬盘状态，精确匹配，支持多个; name - 云硬盘名称，模糊匹配，支持单个;  """, dest='filters', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询云硬盘列表 ''',
        description='''
            查询云硬盘列表。

            示例: jdc disk describe-disks 
        ''',
    )
    def describe_disks(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.DescribeDisksRequest import DescribeDisksRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeDisksRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--disk-spec'], dict(help="""(diskSpec) 创建云硬盘规格 """, dest='diskSpec', required=True)),
            (['--max-count'], dict(help="""(int) 购买实例数量；取值范围：[1,100] """, dest='maxCount', required=True)),
            (['--client-token'], dict(help="""(string) 幂等性校验参数 """, dest='clientToken', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 创建一块或多块云硬盘 ''',
        description='''
            创建一块或多块云硬盘。

            示例: jdc disk create-disks  --disk-spec {"":""} --max-count 0 --client-token xxx
        ''',
    )
    def create_disks(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.CreateDisksRequest import CreateDisksRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateDisksRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询云硬盘信息详情 ''',
        description='''
            查询云硬盘信息详情。

            示例: jdc disk describe-disk  --disk-id xxx
        ''',
    )
    def describe_disk(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.DescribeDiskRequest import DescribeDiskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeDiskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--name'], dict(help="""(string) 云硬盘名称 """, dest='name', required=False)),
            (['--description'], dict(help="""(string) 云硬盘描述，name和description必须要指定一个 """, dest='description', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改云硬盘的名字或描述信息 ''',
        description='''
            修改云硬盘的名字或描述信息。

            示例: jdc disk modify-disk-attribute  --disk-id xxx
        ''',
    )
    def modify_disk_attribute(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.ModifyDiskAttributeRequest import ModifyDiskAttributeRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ModifyDiskAttributeRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除单个云硬盘 ''',
        description='''
            删除单个云硬盘。

            示例: jdc disk delete-disk  --disk-id xxx
        ''',
    )
    def delete_disk(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.DeleteDiskRequest import DeleteDiskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteDiskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--snapshot-id'], dict(help="""(string) 用于恢复云盘的快照ID """, dest='snapshotId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 从已有快照恢复一块云硬盘 ''',
        description='''
            从已有快照恢复一块云硬盘。

            示例: jdc disk restore-disk  --disk-id xxx --snapshot-id xxx
        ''',
    )
    def restore_disk(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.RestoreDiskRequest import RestoreDiskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = RestoreDiskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--disk-size-gb'], dict(help="""(int) 扩容后的云硬盘大小，单位为GiB """, dest='diskSizeGB', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 扩容云硬盘到指定大小 ''',
        description='''
            扩容云硬盘到指定大小。

            示例: jdc disk extend-disk  --disk-id xxx --disk-size-gb 0
        ''',
    )
    def extend_disk(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.ExtendDiskRequest import ExtendDiskRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ExtendDiskRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1, 取值范围：[1,∞) """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20，取值范围：[10,100] """, dest='pageSize', required=False)),
            (['--filters'], dict(help="""(array: filter) snapshotId - 云硬盘快照ID，支持多个; diskId - 生成快照的云硬盘ID，支持多个; status - 快照状态，精确匹配，支持多个,取值为 creating、available、in-use、deleting、error_create、error_delete; name - 快照名称，模糊匹配，支持单个;  """, dest='filters', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询云硬盘快照列表 ''',
        description='''
            查询云硬盘快照列表。

            示例: jdc disk describe-snapshots 
        ''',
    )
    def describe_snapshots(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.DescribeSnapshotsRequest import DescribeSnapshotsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeSnapshotsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--snapshot-spec'], dict(help="""(snapshotSpec) 创建快照规格 """, dest='snapshotSpec', required=True)),
            (['--client-token'], dict(help="""(string) 幂等性校验参数 """, dest='clientToken', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 为指定云硬盘创建快照,新生成的快照的状态为creating ''',
        description='''
            为指定云硬盘创建快照,新生成的快照的状态为creating。

            示例: jdc disk create-snapshot  --snapshot-spec {"":""} --client-token xxx
        ''',
    )
    def create_snapshot(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.CreateSnapshotRequest import CreateSnapshotRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CreateSnapshotRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--snapshot-id'], dict(help="""(string) 快照ID """, dest='snapshotId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询云硬盘快照信息详情 ''',
        description='''
            查询云硬盘快照信息详情。

            示例: jdc disk describe-snapshot  --snapshot-id xxx
        ''',
    )
    def describe_snapshot(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.DescribeSnapshotRequest import DescribeSnapshotRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeSnapshotRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--snapshot-id'], dict(help="""(string) 快照ID """, dest='snapshotId', required=True)),
            (['--name'], dict(help="""(string) 快照名称 """, dest='name', required=False)),
            (['--description'], dict(help="""(string) 快照描述，name和description必须要指定一个 """, dest='description', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改快照的名字或描述信息 ''',
        description='''
            修改快照的名字或描述信息。

            示例: jdc disk modify-snp-attribute  --snapshot-id xxx
        ''',
    )
    def modify_snp_attribute(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.ModifySnpAttributeRequest import ModifySnpAttributeRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = ModifySnpAttributeRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) 地域ID """, dest='regionId', required=False)),
            (['--snapshot-id'], dict(help="""(string) 快照ID """, dest='snapshotId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除单个云硬盘快照:快照状态必须为 available 或 error 状态 ''',
        description='''
            删除单个云硬盘快照:快照状态必须为 available 或 error 状态。

            示例: jdc disk delete-snapshot  --snapshot-id xxx
        ''',
    )
    def delete_snapshot(self):
        client_factory = ClientFactory('disk')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.disk.apis.DeleteSnapshotRequest import DeleteSnapshotRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DeleteSnapshotRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-disks','create-disks','describe-disk','modify-disk-attribute','delete-disk','restore-disk','extend-disk','describe-snapshots','create-snapshot','describe-snapshot','modify-snp-attribute','delete-snapshot',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('disk', self.app.pargs.api)
        skeleton.show()
