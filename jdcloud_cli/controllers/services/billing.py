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


class BillingController(BaseController):
    class Meta:
        label = 'billing'
        help = '计费'
        description = '''
        billing cli 子命令，计费系统API接口。
        OpenAPI文档地址为：https://docs.jdcloud.com/cn/xxx/api/overview
        '''
        stacked_on = 'base'
        stacked_type = 'nested'

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--start-time'], dict(help="""(string) 账期开始时间,不支持跨月查询。格式:yyyy-MM-dd HH:mm:ss """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 账期结束时间,不支持跨月查询。格式:yyyy-MM-dd HH:mm:ss """, dest='endTime',  required=True)),
            (['--app-code'], dict(help="""(string) 产品线代码 """, dest='appCode',  required=False)),
            (['--service-code'], dict(help="""(string) 产品代码 """, dest='serviceCode',  required=False)),
            (['--resource-ids'], dict(help="""(array: string) 资源单id列表,最多支持传入500个 """, dest='resourceIds',  required=False)),
            (['--tags'], dict(help="""(array: object) 标签,JSON格式:[{"k1":"v1"},{"k1":"v2"},{"k2":""}]; 示例:; 选择的标签为, 部门:广告部、部门:物流部、项目; 则传值为:[{"部门":"广告部"},{"部门":"物流部"},{"项目":""}];  """, dest='tags',  required=False)),
            (['--page-index'], dict(help="""(int) pageIndex 分页,默认从1开始 """, dest='pageIndex', type=int, required=False)),
            (['--page-size'], dict(help="""(int) pageSize 每页查询数据条数,最多支持1000条 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询账单资源汇总数据 ''',
        description='''
            查询账单资源汇总数据。

            示例: jdc billing query-bill-summary  --start-time xxx --end-time xxx
        ''',
    )
    def query_bill_summary(self):
        client_factory = ClientFactory('billing')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.billing.apis.QueryBillSummaryRequest import QueryBillSummaryRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = QueryBillSummaryRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) Region ID """, dest='regionId',  required=False)),
            (['--start-time'], dict(help="""(string) 账期开始时间,不支持跨月查询。格式:yyyy-MM-dd HH:mm:ss """, dest='startTime',  required=True)),
            (['--end-time'], dict(help="""(string) 账期结束时间,不支持跨月查询。格式:yyyy-MM-dd HH:mm:ss """, dest='endTime',  required=True)),
            (['--app-code'], dict(help="""(string) 产品线代码 """, dest='appCode',  required=False)),
            (['--service-code'], dict(help="""(string) 产品代码 """, dest='serviceCode',  required=False)),
            (['--billing-type'], dict(help="""(int) 计费类型 1、按配置 2、按用量 3、包年包月 4、按次 """, dest='billingType', type=int, required=False)),
            (['--resource-ids'], dict(help="""(array: string) 资源单id列表,最多支持传入500个 """, dest='resourceIds',  required=False)),
            (['--tags'], dict(help="""(array: object) 标签,JSON格式:[{"k1":"v1"},{"k1":"v2"},{"k2":""}]; 示例:; 选择的标签为, 部门:广告部、部门:物流部、项目; 则传值为:[{"部门":"广告部"},{"部门":"物流部"},{"项目":""}];  """, dest='tags',  required=False)),
            (['--page-index'], dict(help="""(int) pageIndex 分页,默认从1开始 """, dest='pageIndex', type=int, required=False)),
            (['--page-size'], dict(help="""(int) pageSize 每页查询数据条数,最多支持1000条 """, dest='pageSize', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询账单明细数据 ''',
        description='''
            查询账单明细数据。

            示例: jdc billing query-bill-detail  --start-time xxx --end-time xxx
        ''',
    )
    def query_bill_detail(self):
        client_factory = ClientFactory('billing')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.billing.apis.QueryBillDetailRequest import QueryBillDetailRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = QueryBillDetailRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--region-id'], dict(help="""(string) NA """, dest='regionId',  required=False)),
            (['--cmd'], dict(help="""(int) 操作类型 1:创建 2:续费 3:升配 4:删除 """, dest='cmd', type=int, required=True)),
            (['--order-list'], dict(help="""(array: orderPriceProtocol) 计算价格的订单 """, dest='orderList',  required=False)),
            (['--operate-time'], dict(help="""(string) 操作时间(格式为：yyyy-MM-dd HH:mm:ss) """, dest='operateTime',  required=False)),
            (['--promotion-info'], dict(help="""(string) 1:折扣（不需要传） 2:免费活动3:付费活动 4:推荐码 5:会员价 [{"promotionType":1,"activityCode":123},{"promotionType":2,"activityCode":}] """, dest='promotionInfo',  required=False)),
            (['--client-type'], dict(help="""(int) 客户端：1.PC端；2.移动端； """, dest='clientType', type=int, required=False)),
            (['--package-count'], dict(help="""(int) 批量购买时数量 """, dest='packageCount', type=int, required=True)),
            (['--process-type'], dict(help="""(int) 临时升配时必传，3-临时升配 """, dest='processType', type=int, required=False)),
            (['--renew-mode'], dict(help="""(int) 续费方式 0：正常续费  1：续费至统一到期日，续费时必传 """, dest='renewMode', type=int, required=False)),
            (['--unify-expire-day'], dict(help="""(int) 续费统一到期日(1-28)，续费时必传 """, dest='unifyExpireDay', type=int, required=False)),
            (['--total-price-rule'], dict(help="""(int) 计算总价规则 1：计算预付费资源总价（计费类型为包年包月、按次） ；不传计算所有资源总价 """, dest='totalPriceRule', type=int, required=False)),
            (['--input-json'], dict(help='(json) 以json字符串或文件绝对路径形式作为输入参数。\n字符串方式举例：--input-json \'{"field":"value"}\';\n文件格式举例：--input-json file:///xxxx.json', dest='input_json', required=False)),
            (['--jdcloud-header'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='jdcloudHeaders', required=False)),
            (['--headers'], dict(help="""(json) 用户自定义Header，举例：'{"x-jdcloud-security-token":"abc","test":"123"}'""", dest='headers', required=False)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 查询计费价格信息 ''',
        description='''
            查询计费价格信息。

            示例: jdc billing calculate-total-price  --cmd 5 --package-count 5
        ''',
    )
    def calculate_total_price(self):
        client_factory = ClientFactory('billing')
        client = client_factory.get(self.app)
        if client is None:
            return

        try:
            from jdcloud_sdk.services.billing.apis.CalculateTotalPriceRequest import CalculateTotalPriceRequest
            params_dict = collect_user_args(self.app)
            headers = collect_user_headers(self.app)
            req = CalculateTotalPriceRequest(params_dict, headers)
            resp = client.send(req)
            Printer.print_result(resp)
        except ImportError:
            print('{"error":"This api is not supported, please use the newer version"}')
        except Exception as e:
            print(e)

    @expose(
        arguments=[
            (['--api'], dict(help="""(string) api name """, choices=['query-bill-summary','query-bill-detail','calculate-total-price',], required=True)),
        ],
        formatter_class=RawTextHelpFormatter,
        help=''' 生成单个API接口的json骨架空字符串 ''',
        description='''
            生成单个API接口的json骨架空字符串。

            示例: jdc nc generate-skeleton --api describeContainer ''',
    )
    def generate_skeleton(self):
        skeleton = Skeleton('billing', self.app.pargs.api)
        skeleton.show()
