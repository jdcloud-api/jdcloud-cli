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

import unittest
import os
import json


class DomainserviceTest(unittest.TestCase):

    def test_describe_resource_record(self):
        cmd = """python ../../main.py domainservice describe-resource-record  --domain-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_resource_record(self):
        cmd = """python ../../main.py domainservice create-resource-record  --domain-id 'xxx' --req '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_resource_record(self):
        cmd = """python ../../main.py domainservice modify-resource-record  --domain-id 'xxx' --resource-record-id 'xxx' --req '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_resource_record(self):
        cmd = """python ../../main.py domainservice delete-resource-record  --domain-id 'xxx' --resource-record-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_resource_record_status(self):
        cmd = """python ../../main.py domainservice modify-resource-record-status  --domain-id 'xxx' --resource-record-id 'xxx' --action 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_view_tree(self):
        cmd = """python ../../main.py domainservice describe-view-tree  --domain-id 'xxx' --pack-id '5' --view-id '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_batch_set_resource_records(self):
        cmd = """python ../../main.py domainservice batch-set-resource-records  --domain-id 'xxx' --req '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_domains(self):
        cmd = """python ../../main.py domainservice describe-domains  --page-number '5' --page-size '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_domain(self):
        cmd = """python ../../main.py domainservice create-domain  --pack-id '5' --domain-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_domain(self):
        cmd = """python ../../main.py domainservice modify-domain  --domain-id 'xxx' --domain-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_domain(self):
        cmd = """python ../../main.py domainservice delete-domain  --domain-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_domain_query_count(self):
        cmd = """python ../../main.py domainservice describe-domain-query-count  --domain-id 'xxx' --domain-name 'xxx' --start 'xxx' --end 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_domain_query_traffic(self):
        cmd = """python ../../main.py domainservice describe-domain-query-traffic  --domain-id 'xxx' --domain-name 'xxx' --start 'xxx' --end 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_action_log(self):
        cmd = """python ../../main.py domainservice describe-action-log  --page-number '5' --page-size '5' --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_user_view(self):
        cmd = """python ../../main.py domainservice describe-user-view  --domain-id 'xxx' --view-id '5' --page-number '5' --page-size '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_user_view(self):
        cmd = """python ../../main.py domainservice create-user-view  --domain-id 'xxx' --req '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_user_view(self):
        cmd = """python ../../main.py domainservice delete-user-view  --domain-id 'xxx' --req '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_user_view_ip(self):
        cmd = """python ../../main.py domainservice describe-user-view-ip  --domain-id 'xxx' --view-id '5' --page-number '5' --page-size '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_user_view_ip(self):
        cmd = """python ../../main.py domainservice create-user-view-ip  --domain-id 'xxx' --req '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_user_view_ip(self):
        cmd = """python ../../main.py domainservice delete-user-view-ip  --domain-id 'xxx' --req '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_monitor(self):
        cmd = """python ../../main.py domainservice describe-monitor  --domain-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_monitor(self):
        cmd = """python ../../main.py domainservice create-monitor  --domain-id 'xxx' --sub-domain-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_monitor(self):
        cmd = """python ../../main.py domainservice modify-monitor  --domain-id 'xxx' --update-monitor '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_monitor_target(self):
        cmd = """python ../../main.py domainservice describe-monitor-target  --domain-id 'xxx' --sub-domain-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_monitor_target(self):
        cmd = """python ../../main.py domainservice create-monitor-target  --domain-id 'xxx' --sub-domain-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_monitor_status(self):
        cmd = """python ../../main.py domainservice modify-monitor-status  --domain-id 'xxx' --monitor-id 'xxx' --action 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_monitor(self):
        cmd = """python ../../main.py domainservice delete-monitor  --domain-id 'xxx' --monitor-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_monitor_alarm(self):
        cmd = """python ../../main.py domainservice describe-monitor-alarm  --domain-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

