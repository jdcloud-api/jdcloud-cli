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


class JdccsController(BaseController):
    class Meta:
        label = 'jdccs'
        help = 'Cloud Cabinet Service API'
        description = '''
        jdccs cli 子命令，提供云托管服务的相关接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--resource-type'], dict(help="""(string) 资源类型 bandwidth:带宽 """, dest='resourceType',  required=False)),
            (['--resource-id'], dict(help="""(string) 资源ID，指定resourceId时须指定resourceType """, dest='resourceId',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询报警规则列表 ''',
        description='''
            查询报警规则列表。

            示例: jdc jdccs describe-alarms 
        ''',
    )
    def describe_alarms(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeAlarmsRequest import DescribeAlarmsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAlarmsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--alarm-id'], dict(help="""(string) 报警规则ID """, dest='alarmId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询报警规则详情 ''',
        description='''
            查询报警规则详情。

            示例: jdc jdccs describe-alarm  --alarm-id xxx
        ''',
    )
    def describe_alarm(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeAlarmRequest import DescribeAlarmRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAlarmRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--alarm-id'], dict(help="""(string) 报警规则ID """, dest='alarmId',  required=False)),
            (['--start-time'], dict(help="""(int) 查询时间范围的开始时间， UNIX时间戳 """, dest='startTime', type=int, required=False)),
            (['--end-time'], dict(help="""(int) 查询时间范围的结束时间， UNIX时间戳 """, dest='endTime', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 报警历史列表 ''',
        description='''
            报警历史列表。

            示例: jdc jdccs describe-alarm-history 
        ''',
    )
    def describe_alarm_history(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeAlarmHistoryRequest import DescribeAlarmHistoryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeAlarmHistoryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询可用监控项列表 ''',
        description='''
            查询可用监控项列表。

            示例: jdc jdccs describe-metrics 
        ''',
    )
    def describe_metrics(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeMetricsRequest import DescribeMetricsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMetricsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--metric'], dict(help="""(string) 监控项英文标识(id) """, dest='metric',  required=True)),
            (['--resource-id'], dict(help="""(string) 资源ID """, dest='resourceId',  required=True)),
            (['--start-time'], dict(help="""(int) 查询时间范围的开始时间， UNIX时间戳，（机柜电流最多支持最近90天数据查询、带宽流量最多支持最近30天数据查询） """, dest='startTime', type=int, required=True)),
            (['--end-time'], dict(help="""(int) 查询时间范围的结束时间， UNIX时间戳，（机柜电流最多支持最近90天数据查询、带宽流量最多支持最近30天数据查询） """, dest='endTime', type=int, required=True)),
            (['--time-interval'], dict(help="""(string) 时间间隔：分钟m、小时h、天d，如： 10分钟=10m、1小时=1h，3天=3d；默认5m，最小支持5m，最大90d 目前带宽上、下行流量查询，会根据时间范围是否超过2小时，设定时间间隔为1m或5m """, dest='timeInterval',  required=False)),
            (['--ip'], dict(help="""(string) 交换机IP，指定ip时须同时指定port """, dest='ip',  required=False)),
            (['--port'], dict(help="""(string) 端口，指定port时须同时指定ip """, dest='port',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看某资源单个监控项数据 ''',
        description='''
            查看某资源单个监控项数据。

            示例: jdc jdccs describe-metric-data  --idc xxx --metric xxx --resource-id xxx --start-time 0 --end-time 0
        ''',
    )
    def describe_metric_data(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeMetricDataRequest import DescribeMetricDataRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeMetricDataRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--metric'], dict(help="""(string) 监控项英文标识(id) """, dest='metric',  required=True)),
            (['--resource-id'], dict(help="""(string) 资源ID，支持多个resourceId批量查询，每个id用英文竖线分隔 """, dest='resourceId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查看某资源的最后一个监控数据点（目前只支持机柜电流） ''',
        description='''
            查看某资源的最后一个监控数据点（目前只支持机柜电流）。

            示例: jdc jdccs last-downsample  --idc xxx --metric xxx --resource-id xxx
        ''',
    )
    def last_downsample(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.LastDownsampleRequest import LastDownsampleRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = LastDownsampleRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询带宽（出口）流量列表 ''',
        description='''
            查询带宽（出口）流量列表。

            示例: jdc jdccs describe-bandwidth-traffics  --idc xxx
        ''',
    )
    def describe_bandwidth_traffics(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeBandwidthTrafficsRequest import DescribeBandwidthTrafficsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeBandwidthTrafficsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--bandwidth-id'], dict(help="""(string) 带宽（出口）实例ID """, dest='bandwidthId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询带宽（出口）流量（资源）详情 ''',
        description='''
            查询带宽（出口）流量（资源）详情。

            示例: jdc jdccs describe-bandwidth-traffic  --idc xxx --bandwidth-id xxx
        ''',
    )
    def describe_bandwidth_traffic(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeBandwidthTrafficRequest import DescribeBandwidthTrafficRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeBandwidthTrafficRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--resource-id'], dict(help="""(string) 资源ID，支持多个resourceId批量查询，每个id用英文竖线分隔 """, dest='resourceId',  required=True)),
            (['--start-time'], dict(help="""(int) 查询时间范围的开始时间， UNIX时间戳，（支持查询最近30分钟数据且时间范围不超过5分钟） """, dest='startTime', type=int, required=True)),
            (['--end-time'], dict(help="""(int) 查询时间范围的结束时间， UNIX时间戳，（支持查询最近30分钟数据且时间范围不超过5分钟） """, dest='endTime', type=int, required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 根据IP网段查询流量采样数据 ''',
        description='''
            根据IP网段查询流量采样数据。

            示例: jdc jdccs describe-traffic-sampling  --resource-id xxx --start-time 0 --end-time 0
        ''',
    )
    def describe_traffic_sampling(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeTrafficSamplingRequest import DescribeTrafficSamplingRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeTrafficSamplingRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询IDC机房列表 ''',
        description='''
            查询IDC机房列表。

            示例: jdc jdccs describe-idcs 
        ''',
    )
    def describe_idcs(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeIdcsRequest import DescribeIdcsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIdcsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) roomNo - 房间号，精确匹配，支持多个;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询机房房间号列表 ''',
        description='''
            查询机房房间号列表。

            示例: jdc jdccs describe-rooms  --idc xxx
        ''',
    )
    def describe_rooms(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeRoomsRequest import DescribeRoomsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeRoomsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) roomNo - 房间号，精确匹配，支持多个; cabinetId - 机柜ID，精确匹配，支持多个;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询机柜列表 ''',
        description='''
            查询机柜列表。

            示例: jdc jdccs describe-cabinets  --idc xxx
        ''',
    )
    def describe_cabinets(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeCabinetsRequest import DescribeCabinetsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeCabinetsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--cabinet-id'], dict(help="""(string) 机柜实例ID """, dest='cabinetId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询机柜详情 ''',
        description='''
            查询机柜详情。

            示例: jdc jdccs describe-cabinet  --idc xxx --cabinet-id xxx
        ''',
    )
    def describe_cabinet(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeCabinetRequest import DescribeCabinetRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeCabinetRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--cabinet-id'], dict(help="""(string) 机柜ID """, dest='cabinetId',  required=False)),
            (['--filters'], dict(help="""(array: filter) deviceId - 设备实例ID，精确匹配，支持多个; snNo - 设备SN号，精确匹配，支持多个;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询设备列表 ''',
        description='''
            查询设备列表。

            示例: jdc jdccs describe-devices  --idc xxx
        ''',
    )
    def describe_devices(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeDevicesRequest import DescribeDevicesRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeDevicesRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--device-id'], dict(help="""(string) 设备实例ID """, dest='deviceId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询设备详情 ''',
        description='''
            查询设备详情。

            示例: jdc jdccs describe-device  --idc xxx --device-id xxx
        ''',
    )
    def describe_device(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeDeviceRequest import DescribeDeviceRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeDeviceRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) ipId - 公网IP实例ID，精确匹配，支持多个;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询公网IP列表 ''',
        description='''
            查询公网IP列表。

            示例: jdc jdccs describe-ips  --idc xxx
        ''',
    )
    def describe_ips(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeIpsRequest import DescribeIpsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeIpsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--filters'], dict(help="""(array: filter) bandwidthId - 带宽实例IID，精确匹配，支持多个;  """, dest='filters',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询带宽（出口）列表 ''',
        description='''
            查询带宽（出口）列表。

            示例: jdc jdccs describe-bandwidths  --idc xxx
        ''',
    )
    def describe_bandwidths(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeBandwidthsRequest import DescribeBandwidthsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeBandwidthsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--idc'], dict(help="""(string) IDC机房ID """, dest='idc',  required=True)),
            (['--bandwidth-id'], dict(help="""(string) 带宽（出口）实例ID """, dest='bandwidthId',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询带宽（出口）详情 ''',
        description='''
            查询带宽（出口）详情。

            示例: jdc jdccs describe-bandwidth  --idc xxx --bandwidth-id xxx
        ''',
    )
    def describe_bandwidth(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeBandwidthRequest import DescribeBandwidthRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeBandwidthRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--page-number'], dict(help="""(int) 页码, 默认为1 """, dest='pageNumber', type=int, required=False)),
            (['--page-size'], dict(help="""(int) 分页大小，默认为20 """, dest='pageSize', type=int, required=False)),
            (['--type'], dict(help="""(string) 工单TAB类型 pendingProcess:待我处理 pendingReview:待审核 processing:处理中 all:全部(默认) """, dest='type',  required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询工单列表 ''',
        description='''
            查询工单列表。

            示例: jdc jdccs describe-tickets 
        ''',
    )
    def describe_tickets(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeTicketsRequest import DescribeTicketsRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeTicketsRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--ticket-no'], dict(help="""(string) 工单编号 """, dest='ticketNo',  required=True)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询工单详情 ''',
        description='''
            查询工单详情。

            示例: jdc jdccs describe-ticket  --ticket-no xxx
        ''',
    )
    def describe_ticket(self):
        client_factory = ClientFactory('jdccs')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.jdccs.apis.DescribeTicketRequest import DescribeTicketRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = DescribeTicketRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['describe-alarms','describe-alarm','describe-alarm-history','describe-metrics','describe-metric-data','last-downsample','describe-bandwidth-traffics','describe-bandwidth-traffic','describe-traffic-sampling','describe-idcs','describe-rooms','describe-cabinets','describe-cabinet','describe-devices','describe-device','describe-ips','describe-bandwidths','describe-bandwidth','describe-tickets','describe-ticket',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('jdccs', self.app.pargs.api)
        skeleton.show()
