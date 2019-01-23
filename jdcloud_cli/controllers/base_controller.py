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

from argparse import RawTextHelpFormatter
from jdcloud_cli.cement.ext.ext_argparse import ArgparseController
from jdcloud_cli.version import VERSION


class BaseController(ArgparseController):
    class Meta:
        label = 'base'
        arguments = [
            (['--output'], dict(help='output format', choices=['json'], default='json')),
            (['-v', '--version'], dict(action='version', version=VERSION)),
        ]
        argument_formatter = RawTextHelpFormatter
        description = '''
        京东云CLI使用方法简介:
        
        1) 配置默认Profile
           jdc configure add --access-key your-ak --secret-key your-sk
           说明：access-key和secret-key可以从京东云控制台申请开通。默认为华北区域。
           
        2) 配置自动完成，方便输入指令。输入两次TAB键可联想出子命令或参数。
           a) Linux & Mac
              echo 'eval "$(register-python-argcomplete jdc)"' >> .bashrc
              echo 'export COLUMNS=100' >> .bashrc
              source ~/.bashrc
            
           b) Windows（在git bash中执行）
              curl https://raw.githubusercontent.com/jdcloud-api/jdcloud-cli/master/jdcloud_cli/resources/jdc.rc > ~/jdc.rc
              echo 'source ~/jdc.rc' >> ~/.bashrc
              echo 'export PYTHONIOENCODING="UTF-8"' >> ~/.bashrc
              source ~/.bashrc
                
        3）使用各产品线命令访问资源，如：
           jdc vm describe-instances
           
           另外，可以使用 --input-json 参数创建资源。支持两种方式：
           a）直接输入json串
              jdc nc create-container --input-json 
                '{
                    "maxCount": 1, 
                    "containerSpec": 
                    {
                        //此处省略具体字段，详情请见京东云OpenAPI官方文档
                    }
                }'
                
           b）指定json文件方式
              jdc nc create-container --input-json 'file:///admin/create.json'
              
           注意：
           json串的获取可以使用各产品线子命令下的 generate-skeleton 获取，如：
           jdc vm generate-skeleton --api create-instances
           
        4）支持Linux、Mac、Windows中的容器交互式命令，如：
           jdc nc attach --container-id c-poqjwenfx 
           
           注意：退出容器时请使用Ctrl+PQ快捷键，若使用exit命令或直接关闭终端，容器会异常终止。
           解决方法为，使用stop-container、start-container命令重启容器。
           
        5）如果发现Bug，请使用以下命令获取debug信息，并提交到GitHub项目中。
           jdc --debug sub-command sub-command --parameters
           项目地址为：https://github.com/jdcloud-api/jdcloud-cli/issues

        6）更详细使用说明，请见京东云官方帮助文档：
           https://www.jdcloud.com/help/faq?act=3
        '''

    def default(self):
        print("Welcome to use JDCloud CLI! Please use -h to visit help. Enjoy!")
