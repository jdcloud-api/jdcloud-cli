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


class ClouddnsserviceController(BaseController):
    class Meta:
        label = 'clouddnsservice'
        help = '使用该子命令操作clouddnsservice相关资源'
        description = '''
        clouddnsservice cli 子命令，可以使用该子命令操作clouddnsservice相关资源。
        OpenAPI文档地址为：https://www.jdcloud.com/help/detail/421/isCatalog/0
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--page-number'], dict(help="""(int) 当前页数，起始值为1，默认为1 """, dest='pageNumber', required=True)),
            (['--page-size'], dict(help="""(int) 分页查询时设置的每页行数 """, dest='pageSize', required=True)),
            (['--domain-name'], dict(help="""(string) 关键字，按照”%domainName%”模式搜索主域名 """, dest='domainName', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询用户名下的主域名列表 ''',
        description='''
            查询用户名下的主域名列表。

            示例: jdc clouddnsservice get-domains  --page-number 0 --page-size 0
        ''',
    )
    def get_domains(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.GetDomainsRequest import GetDomainsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetDomainsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--pack-id'], dict(help="""(int) 套餐类型, 0免费 ,1企业版, 2高级版 """, dest='packId', required=True)),
            (['--domain-name'], dict(help="""(string) 域名 """, dest='domainName', required=True)),
            (['--domain-id'], dict(help="""(int) 域名ID，升级高级版必填 """, dest='domainId', required=False)),
            (['--buy-type'], dict(help="""(int) 1新购买、2升级，高级版必填 """, dest='buyType', required=False)),
            (['--time-span'], dict(help="""(int) 1-3 ，时长，高级版必填 """, dest='timeSpan', required=False)),
            (['--time-unit'], dict(help="""(int) 时间单位，高级版必填 """, dest='timeUnit', required=False)),
            (['--billing-type'], dict(help="""(int) 计费类型，高级版必填 """, dest='billingType', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加主域名 ''',
        description='''
            添加主域名。

            示例: jdc clouddnsservice add-domain  --pack-id 0 --domain-name xxx
        ''',
    )
    def add_domain(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.AddDomainRequest import AddDomainRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AddDomainRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(int) 域名ID """, dest='domainId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 删除主域名 ''',
        description='''
            删除主域名。

            示例: jdc clouddnsservice del-domain  --domain-id 0
        ''',
    )
    def del_domain(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.DelDomainRequest import DelDomainRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DelDomainRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-name'], dict(help="""(string) 域名 """, dest='domainName', required=True)),
            (['--id'], dict(help="""(int) 域名ID """, dest='id', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改主域名 ''',
        description='''
            修改主域名。

            示例: jdc clouddnsservice update-domain  --domain-name xxx --id 0
        ''',
    )
    def update_domain(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.UpdateDomainRequest import UpdateDomainRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateDomainRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--action'], dict(help="""(string) 查询动作，"query"查询流量，"resolve"解析流量 """, dest='action', required=True)),
            (['--domain-name'], dict(help="""(string) 域名 """, dest='domainName', required=True)),
            (['--start'], dict(help="""(string) 起始时间, UTC时间例如2017-11-10T23:00:00Z """, dest='start', required=True)),
            (['--end'], dict(help="""(string) 终止时间, UTC时间例如2017-11-10T23:00:00Z """, dest='end', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看域名的查询流量 ''',
        description='''
            查看域名的查询流量。

            示例: jdc clouddnsservice get-domain-statistics  --domain-id xxx --action xxx --domain-name xxx --start xxx --end xxx
        ''',
    )
    def get_domain_statistics(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.GetDomainStatisticsRequest import GetDomainStatisticsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetDomainStatisticsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--page-index'], dict(help="""(int) 当前页数，起始值为1，默认为1 """, dest='pageIndex', required=False)),
            (['--page-size'], dict(help="""(int) 分页查询时设置的每页行数 """, dest='pageSize', required=False)),
            (['--search-value'], dict(help="""(string) 查询的值 """, dest='searchValue', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看主域名的监控项的配置以及状态 ''',
        description='''
            查看主域名的监控项的配置以及状态。

            示例: jdc clouddnsservice get-monitor  --domain-id xxx
        ''',
    )
    def get_monitor(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.GetMonitorRequest import GetMonitorRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetMonitorRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--sub-domain-name'], dict(help="""(string) 子域名 """, dest='subDomainName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加子域名的监控项，采用默认配置 ''',
        description='''
            添加子域名的监控项，采用默认配置。

            示例: jdc clouddnsservice add-monitor  --domain-id xxx --sub-domain-name xxx
        ''',
    )
    def add_monitor(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.AddMonitorRequest import AddMonitorRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AddMonitorRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--sub-domain-name'], dict(help="""(string) 子域名 """, dest='subDomainName', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询子域名的可用监控对象 ''',
        description='''
            查询子域名的可用监控对象。

            示例: jdc clouddnsservice get-targets  --domain-id xxx --sub-domain-name xxx
        ''',
    )
    def get_targets(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.GetTargetsRequest import GetTargetsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetTargetsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--sub-domain-name'], dict(help="""(string) 子域名 """, dest='subDomainName', required=True)),
            (['--targets'], dict(help="""(array: string) 子域名可用监控对象的数组 """, dest='targets', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加子域名的某些特定监控对象为监控项 ''',
        description='''
            添加子域名的某些特定监控对象为监控项。

            示例: jdc clouddnsservice add-monitor-target  --domain-id xxx --sub-domain-name xxx
        ''',
    )
    def add_monitor_target(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.AddMonitorTargetRequest import AddMonitorTargetRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AddMonitorTargetRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--action'], dict(help="""(string) 删除del, 暂停stop, 开启start, 手动恢复recover，手动切换switch """, dest='action', required=True)),
            (['--ids'], dict(help="""(array: int) 监控项ID """, dest='ids', required=True)),
            (['--switch-target'], dict(help="""(string) 监控项的主机值, 手动切换时必填 """, dest='switchTarget', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 监控项的操作，包括：删除，暂停，启动, 手动恢复, 手动切换 ''',
        description='''
            监控项的操作，包括：删除，暂停，启动, 手动恢复, 手动切换。

            示例: jdc clouddnsservice operate-monitor  --domain-id xxx --action xxx --ids [0]
        ''',
    )
    def operate_monitor(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.OperateMonitorRequest import OperateMonitorRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = OperateMonitorRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--update-monitor'], dict(help="""(updateMonitor) 监控项设置信息 """, dest='updateMonitor', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 域名的监控项修改 ''',
        description='''
            域名的监控项修改。

            示例: jdc clouddnsservice update-monitor  --domain-id xxx --update-monitor {"":""}
        ''',
    )
    def update_monitor(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.UpdateMonitorRequest import UpdateMonitorRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateMonitorRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--page-index'], dict(help="""(int) 当前页数，起始值为1，默认为1 """, dest='pageIndex', required=False)),
            (['--page-size'], dict(help="""(int) 分页查询时设置的每页行数 """, dest='pageSize', required=False)),
            (['--search-value'], dict(help="""(string) 关键字 """, dest='searchValue', required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 主域名的监控项的报警信息 ''',
        description='''
            主域名的监控项的报警信息。

            示例: jdc clouddnsservice get-monitor-alarm-info  --domain-id xxx
        ''',
    )
    def get_monitor_alarm_info(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.GetMonitorAlarmInfoRequest import GetMonitorAlarmInfoRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetMonitorAlarmInfoRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询某个主域名的解析记录 ''',
        description='''
            查询某个主域名的解析记录。

            示例: jdc clouddnsservice search-rr  --domain-id xxx
        ''',
    )
    def search_rr(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.SearchRRRequest import SearchRRRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = SearchRRRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--load-mode'], dict(help="""(int) 展示方式 """, dest='loadMode', required=False)),
            (['--pack-id'], dict(help="""(int) 套餐ID """, dest='packId', required=True)),
            (['--view-id'], dict(help="""(int) view ID，默认为0 """, dest='viewId', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询DNS所有解析线路 ''',
        description='''
            查询DNS所有解析线路。

            示例: jdc clouddnsservice get-view-tree  --domain-id xxx --pack-id 0 --view-id 0
        ''',
    )
    def get_view_tree(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.GetViewTreeRequest import GetViewTreeRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = GetViewTreeRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--req'], dict(help="""(addRR) RR参数 """, dest='req', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 添加域名解析 ''',
        description='''
            添加域名解析。

            示例: jdc clouddnsservice add-rr  --domain-id xxx --req {"":""}
        ''',
    )
    def add_rr(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.AddRRRequest import AddRRRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = AddRRRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--req'], dict(help="""(updateRR) updateRR参数 """, dest='req', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 修改主域名的某个解析记录 ''',
        description='''
            修改主域名的某个解析记录。

            示例: jdc clouddnsservice update-rr  --domain-id xxx --req {"":""}
        ''',
    )
    def update_rr(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.UpdateRRRequest import UpdateRRRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = UpdateRRRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId', required=False)),
            (['--domain-id'], dict(help="""(string) 域名ID """, dest='domainId', required=True)),
            (['--ids'], dict(help="""(array: int) 需要操作的解析记录ID """, dest='ids', required=True)),
            (['--action'], dict(help="""(string) 操作类型，on/off/del，分别是启用、停用、删除解析记录 """, dest='action', required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 启用、停用、删除主域名下的解析记录 ''',
        description='''
            启用、停用、删除主域名下的解析记录。

            示例: jdc clouddnsservice operate-rr  --domain-id xxx --ids [0] --action xxx
        ''',
    )
    def operate_rr(self):
        client_factory = ClientFactory('clouddnsservice')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.clouddnsservice.apis.OperateRRRequest import OperateRRRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = OperateRRRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print '{"error":"This api is not supported, please use the newer version"}'
        except Exception as e:
            print e.message

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['get-domains','add-domain','del-domain','update-domain','get-domain-statistics','get-monitor','add-monitor','get-targets','add-monitor-target','operate-monitor','update-monitor','get-monitor-alarm-info','search-rr','get-view-tree','add-rr','update-rr','operate-rr',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('clouddnsservice', self.app.pargs.api)
        skeleton.show()
