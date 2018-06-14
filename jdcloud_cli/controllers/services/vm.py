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

from cement.ext.ext_argparse import expose
from jdcloud_cli.controllers.base_controller import BaseController
from jdcloud_cli.client_factory import ClientFactory
from jdcloud_cli.parameter_builder import collect_user_args
from jdcloud_cli.printer import Printer
from jdcloud_cli.skeleton import Skeleton


class VmController(BaseController):
    class Meta:
        label = 'vm'
        help = '使用该子命令操作vm相关资源'
        description = 'vm cli 子命令，可以使用该子命令操作vm相关资源'
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-id'], dict(help="""(string) Image ID """, dest='imageId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询镜像信息 """,
        description=""" 查询镜像信息。
            示例: jdc vm describe-image  --image-id xxx
        """,
    )
    def describe_image(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeImageRequest import DescribeImageRequest
            params_dict = collect_user_args(self.app)
            req = DescribeImageRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-id'], dict(help="""(string) Image ID """, dest='imageId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 删除私有镜像 """,
        description=""" 删除私有镜像。
            示例: jdc vm delete-image  --image-id xxx
        """,
    )
    def delete_image(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DeleteImageRequest import DeleteImageRequest
            params_dict = collect_user_args(self.app)
            req = DeleteImageRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-source'], dict(help="""(string) 镜像来源：public、shared、thirdparty、private，如果没有指定ids参数，此参数必传 """, dest='imageSource', required=False)),
            (['--platform'], dict(help="""(string) 操作系统平台: Windows Server、CentOS、Ubuntu """, dest='platform', required=False)),
            (['--ids'], dict(help="""(array: string) 镜像ID列表，如果指定了此参数，其它参数可为空 """, dest='ids', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询镜像资源信息列表 """,
        description=""" 查询镜像资源信息列表。
            示例: jdc vm describe-images 
        """,
    )
    def describe_images(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeImagesRequest import DescribeImagesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeImagesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-id'], dict(help="""(string) Image ID """, dest='imageId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询镜像限制 """,
        description=""" 查询镜像限制。
            示例: jdc vm describe-image-constraints  --image-id xxx
        """,
    )
    def describe_image_constraints(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeImageConstraintsRequest import DescribeImageConstraintsRequest
            params_dict = collect_user_args(self.app)
            req = DescribeImageConstraintsRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-id'], dict(help="""(string) Image ID """, dest='imageId', required=True)),
            (['--pins'], dict(help="""(array: string) 需要共享的帐户 """, dest='pins', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" "共享镜像，最多可共享给20个帐户"; "打包镜像暂不支持共享"; "不能操作非私有镜像"; "不能共享给自己";  """,
        description=""" "共享镜像，最多可共享给20个帐户"; "打包镜像暂不支持共享"; "不能操作非私有镜像"; "不能共享给自己"; 。
            示例: jdc vm share-image  --image-id xxx
        """,
    )
    def share_image(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.ShareImageRequest import ShareImageRequest
            params_dict = collect_user_args(self.app)
            req = ShareImageRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-id'], dict(help="""(string) Image ID """, dest='imageId', required=True)),
            (['--pins'], dict(help="""(array: string) 需要取消的帐户 """, dest='pins', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 取消共享镜像，不能操作非私有镜像 """,
        description=""" 取消共享镜像，不能操作非私有镜像。
            示例: jdc vm un-share-image  --image-id xxx
        """,
    )
    def un_share_image(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.UnShareImageRequest import UnShareImageRequest
            params_dict = collect_user_args(self.app)
            req = UnShareImageRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--image-id'], dict(help="""(string) Image ID """, dest='imageId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询镜像共享帐户列表，不能操作非私有镜像 """,
        description=""" 查询镜像共享帐户列表，不能操作非私有镜像。
            示例: jdc vm describe-image-members  --image-id xxx
        """,
    )
    def describe_image_members(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeImageMembersRequest import DescribeImageMembersRequest
            params_dict = collect_user_args(self.app)
            req = DescribeImageMembersRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--page-number'], dict(help="""(int) 页码；默认为1 """, dest='pageNumber', required=False)),
            (['--page-size'], dict(help="""(int) 分页大小；默认为20；取值范围[10, 100] """, dest='pageSize', required=False)),
            (['--tags'], dict(help="""(array: tagFilter) Tag筛选条件 """, dest='tags', required=False)),
            (['--filters'], dict(help="""(array: filter) instanceId - 实例ID，精确匹配，支持多个; privateIpAddress - 主网卡IP地址，模糊匹配，支持单个; az - 可用区，精确匹配，支持多个; vpcId - 私有网络ID，精确匹配，支持多个; status - 云主机状态，精确匹配，支持多个; name - 实例名称，模糊匹配，支持单个; imageId - 镜像ID，模糊匹配，支持单个;  """, dest='filters', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询云主机列表 """,
        description=""" 查询云主机列表。
            示例: jdc vm describe-instances 
        """,
    )
    def describe_instances(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeInstancesRequest import DescribeInstancesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstancesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-spec'], dict(help="""(instanceSpec) 创建主机规格 """, dest='instanceSpec', required=True)),
            (['--max-count'], dict(help="""(int) 购买实例数量；取值范围：[1,100]，默认为1 """, dest='maxCount', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 创建一台或多台指定配置的实例 """,
        description=""" 创建一台或多台指定配置的实例。
            示例: jdc vm create-instances  --instance-spec {"":""}
        """,
    )
    def create_instances(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.CreateInstancesRequest import CreateInstancesRequest
            params_dict = collect_user_args(self.app)
            req = CreateInstancesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询云主机详情 """,
        description=""" 查询云主机详情。
            示例: jdc vm describe-instance  --instance-id xxx
        """,
    )
    def describe_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeInstanceRequest import DescribeInstanceRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" "删除单个实例"; "主机状态必须为停止状态、同时主机没有未完成的任务才可删除"; "包年包月未到期的主机不能删除"; "如果主机中挂载了数据盘，并且设置了AutoDelete属性为true，那么数据盘会随主机一起删除";  """,
        description=""" "删除单个实例"; "主机状态必须为停止状态、同时主机没有未完成的任务才可删除"; "包年包月未到期的主机不能删除"; "如果主机中挂载了数据盘，并且设置了AutoDelete属性为true，那么数据盘会随主机一起删除"; 。
            示例: jdc vm delete-instance  --instance-id xxx
        """,
    )
    def delete_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DeleteInstanceRequest import DeleteInstanceRequest
            params_dict = collect_user_args(self.app)
            req = DeleteInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 停止单个实例，只能停止running状态的实例，主机没有未完成的任务才可停止 """,
        description=""" 停止单个实例，只能停止running状态的实例，主机没有未完成的任务才可停止。
            示例: jdc vm stop-instance  --instance-id xxx
        """,
    )
    def stop_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.StopInstanceRequest import StopInstanceRequest
            params_dict = collect_user_args(self.app)
            req = StopInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 启动单个实例，只能启动stopped状态的实例，主机没有未完成的任务才可启动 """,
        description=""" 启动单个实例，只能启动stopped状态的实例，主机没有未完成的任务才可启动。
            示例: jdc vm start-instance  --instance-id xxx
        """,
    )
    def start_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.StartInstanceRequest import StartInstanceRequest
            params_dict = collect_user_args(self.app)
            req = StartInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 重启单个实例，只能重启running状态的实例，主机没有未完成的任务才可重启 """,
        description=""" 重启单个实例，只能重启running状态的实例，主机没有未完成的任务才可重启。
            示例: jdc vm reboot-instance  --instance-id xxx
        """,
    )
    def reboot_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.RebootInstanceRequest import RebootInstanceRequest
            params_dict = collect_user_args(self.app)
            req = RebootInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--elastic-ip-id'], dict(help="""(string) 弹性IP ID """, dest='elasticIpId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 云主机绑定公网IP 绑定的是主网卡、主内网IP对应的弹性IP """,
        description=""" 云主机绑定公网IP 绑定的是主网卡、主内网IP对应的弹性IP。
            示例: jdc vm associate-elastic-ip  --instance-id xxx --elastic-ip-id xxx
        """,
    )
    def associate_elastic_ip(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.AssociateElasticIpRequest import AssociateElasticIpRequest
            params_dict = collect_user_args(self.app)
            req = AssociateElasticIpRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--elastic-ip-id'], dict(help="""(string) 弹性IP ID """, dest='elasticIpId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 云主机解绑公网IP 解绑的是主网卡、主内网IP对应的弹性IP """,
        description=""" 云主机解绑公网IP 解绑的是主网卡、主内网IP对应的弹性IP。
            示例: jdc vm disassociate-elastic-ip  --instance-id xxx --elastic-ip-id xxx
        """,
    )
    def disassociate_elastic_ip(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DisassociateElasticIpRequest import DisassociateElasticIpRequest
            params_dict = collect_user_args(self.app)
            req = DisassociateElasticIpRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--name'], dict(help="""(string) 名称 """, dest='name', required=True)),
            (['--description'], dict(help="""(string) 描述 """, dest='description', required=True)),
            (['--data-disks'], dict(help="""(array: instanceDiskAttachmentSpec) 数据盘列表，如果指定，则随镜像一起打包创建快照，实际最多不能超过4个 """, dest='dataDisks', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" "虚机创建私有镜像"; "虚机状态必须为stopped"; "如果虚机上有挂载数据盘，默认会将数据盘创建快照，生成打包镜像"; "主机没有未完成的任务才可制作镜像";  """,
        description=""" "虚机创建私有镜像"; "虚机状态必须为stopped"; "如果虚机上有挂载数据盘，默认会将数据盘创建快照，生成打包镜像"; "主机没有未完成的任务才可制作镜像"; 。
            示例: jdc vm create-image  --instance-id xxx --name xxx --description xxx
        """,
    )
    def create_image(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.CreateImageRequest import CreateImageRequest
            params_dict = collect_user_args(self.app)
            req = CreateImageRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--device-name'], dict(help="""(string) 逻辑挂载点[vdb,vdc,vdd,vde,vdf,vdg,vdh] """, dest='deviceName', required=True)),
            (['--auto-delete'], dict(help="""(bool) 当删除主机时，是否自动关联删除此硬盘，默认False，只支持按配置计费 """, dest='autoDelete', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 云主机挂载硬盘，主机和云盘没有未完成的任务时才可挂载，一个主机上最多可挂载4块数据盘 """,
        description=""" 云主机挂载硬盘，主机和云盘没有未完成的任务时才可挂载，一个主机上最多可挂载4块数据盘。
            示例: jdc vm attach-disk  --instance-id xxx --disk-id xxx --device-name xxx
        """,
    )
    def attach_disk(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.AttachDiskRequest import AttachDiskRequest
            params_dict = collect_user_args(self.app)
            req = AttachDiskRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--disk-id'], dict(help="""(string) 云硬盘ID """, dest='diskId', required=True)),
            (['--force'], dict(help="""(bool) 强制缷载，默认False """, dest='force', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 云主机缷载硬盘，主机和云盘没有未完成的任务时才可缷载 """,
        description=""" 云主机缷载硬盘，主机和云盘没有未完成的任务时才可缷载。
            示例: jdc vm detach-disk  --instance-id xxx --disk-id xxx
        """,
    )
    def detach_disk(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DetachDiskRequest import DetachDiskRequest
            params_dict = collect_user_args(self.app)
            req = DetachDiskRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--name'], dict(help="""(string) 名称；名称和描述必传其中一个；不为空且只允许中文、数字、大小写字母、英文下划线“_”及中划线“-”，长度不超过32字符 """, dest='name', required=False)),
            (['--description'], dict(help="""(string) 描述；名称和描述必传其中一个；长度不超过256个字符 """, dest='description', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 修改主机信息 """,
        description=""" 修改主机信息。
            示例: jdc vm modify-instance-attribute  --instance-id xxx
        """,
    )
    def modify_instance_attribute(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.ModifyInstanceAttributeRequest import ModifyInstanceAttributeRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstanceAttributeRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--password'], dict(help="""(string) "密码，长度8-30个字符"; "a)不能出现的字符或完整单词，如下：jd、JD、360、bug、BUG、com、COM、cloud、CLOUD、password、PASSWORD"; "b)不能出现连续三位及三位以上数字，例：123、987"; "c)不能出现连续三位及三位以上的字母，例：abc、CBA、bcde、cdef"; "d)不能出现三位及三位以上键位顺序（仅包括字母），例：qaz、tfc、wsx、xsw、qwert、trewq"; "e)密码中不能出现自己的用户名"; "g)至少同时包含三类（大写字母，小写字母，数字和特殊字符，特殊字符为 ** ()`~!@#$%&_-+={}[]:\";'<>,.?/）*|";  """, dest='password', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 修改主机密码，主机没有未完成的任务时才可操作 """,
        description=""" 修改主机密码，主机没有未完成的任务时才可操作。
            示例: jdc vm modify-instance-password  --instance-id xxx --password xxx
        """,
    )
    def modify_instance_password(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.ModifyInstancePasswordRequest import ModifyInstancePasswordRequest
            params_dict = collect_user_args(self.app)
            req = ModifyInstancePasswordRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询主机vnc """,
        description=""" 查询主机vnc。
            示例: jdc vm describe-instance-vnc-url  --instance-id xxx
        """,
    )
    def describe_instance_vnc_url(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeInstanceVncUrlRequest import DescribeInstanceVncUrlRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstanceVncUrlRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--instance-type'], dict(help="""(string) 实例规格 """, dest='instanceType', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" "云主机变更实例规格，需要关机操作"; "16年创建的云盘做系统盘的主机，一代与二代实例类型不允许相互调整"; "本地盘做系统盘的主机，一代与二代实例类型不允许相互调整"; "ag中的主机，一代与二代实例类型不允许相互调整"; "变更后实例规格的网卡数量限制，要支持当前主机的网卡数量，如不支持，需要缷载网卡后再变更实例规格";  """,
        description=""" "云主机变更实例规格，需要关机操作"; "16年创建的云盘做系统盘的主机，一代与二代实例类型不允许相互调整"; "本地盘做系统盘的主机，一代与二代实例类型不允许相互调整"; "ag中的主机，一代与二代实例类型不允许相互调整"; "变更后实例规格的网卡数量限制，要支持当前主机的网卡数量，如不支持，需要缷载网卡后再变更实例规格"; 。
            示例: jdc vm resize-instance  --instance-id xxx --instance-type xxx
        """,
    )
    def resize_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.ResizeInstanceRequest import ResizeInstanceRequest
            params_dict = collect_user_args(self.app)
            req = ResizeInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--instance-id'], dict(help="""(string) Instance ID """, dest='instanceId', required=True)),
            (['--password'], dict(help="""(string) 云主机密码 """, dest='password', required=True)),
            (['--image-id'], dict(help="""(string) 镜像ID """, dest='imageId', required=False)),
            (['--key-names'], dict(help="""(array: string) 密钥对名称；当前只支持一个 """, dest='keyNames', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 云主机使用指定镜像重置实例镜像，需要关机操作， """,
        description=""" 云主机使用指定镜像重置实例镜像，需要关机操作，。
            示例: jdc vm rebuild-instance  --instance-id xxx --password xxx
        """,
    )
    def rebuild_instance(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.RebuildInstanceRequest import RebuildInstanceRequest
            params_dict = collect_user_args(self.app)
            req = RebuildInstanceRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--filters'], dict(help="""(array: filter) instanceTypes - 实例类型，精确匹配，支持多个; az - 可用区，精确匹配，支持多个;  """, dest='filters', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询实例类型资源信息列表 """,
        description=""" 查询实例类型资源信息列表。
            示例: jdc vm describe-instance-types 
        """,
    )
    def describe_instance_types(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeInstanceTypesRequest import DescribeInstanceTypesRequest
            params_dict = collect_user_args(self.app)
            req = DescribeInstanceTypesRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--filters'], dict(help="""(array: filter) resourceTypes - 资源类型，支持多个[instance，keypair，image，instanceTemplate];  """, dest='filters', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。字符串方式举例：--input-json \'{"field":"value"}\';文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
        ],
        help=""" 查询（虚机、镜像、密钥、模板）配额 """,
        description=""" 查询（虚机、镜像、密钥、模板）配额。
            示例: jdc vm describe-quotas 
        """,
    )
    def describe_quotas(self):
        client_factory = ClientFactory('vm')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.vm.apis.DescribeQuotasRequest import DescribeQuotasRequest
            params_dict = collect_user_args(self.app)
            req = DescribeQuotasRequest(params_dict)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-image','delete-image','describe-images','describe-image-constraints','share-image','un-share-image','describe-image-members','describe-instances','create-instances','describe-instance','delete-instance','stop-instance','start-instance','reboot-instance','associate-elastic-ip','disassociate-elastic-ip','create-image','attach-disk','detach-disk','modify-instance-attribute','modify-instance-password','describe-instance-vnc-url','resize-instance','rebuild-instance','describe-instance-types','describe-quotas',], required=True)),
        ],
        help=""" 生成单个API接口的json骨架空字符串 """,
        description=""" 生成单个API接口的json骨架空字符串。示例: jdc nc generate-skeleton --api describeContainer """,
    )
    def generate_skeleton(self):
        skeleton = Skeleton('vm', self.app.pargs.api)
        skeleton.show()
