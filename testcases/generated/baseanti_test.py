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


class BaseantiTest(unittest.TestCase):

    def test_describe_attack_logs(self):
        cmd = """python ../../main.py baseanti describe-attack-logs  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_attack_statistics(self):
        cmd = """python ../../main.py baseanti describe-attack-statistics  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_attack_type_count(self):
        cmd = """python ../../main.py baseanti describe-attack-type-count  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_monitor_flow(self):
        cmd = """python ../../main.py baseanti describe-ip-monitor-flow  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_resources(self):
        cmd = """python ../../main.py baseanti describe-ip-resources """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ip_resources(self):
        cmd = """python ../../main.py baseanti describe-elastic-ip-resources """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cps_ip_resources(self):
        cmd = """python ../../main.py baseanti describe-cps-ip-resources """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ccs_ip_resources(self):
        cmd = """python ../../main.py baseanti describe-ccs-ip-resources """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_resource_info(self):
        cmd = """python ../../main.py baseanti describe-ip-resource-info  --ip 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_safety_info(self):
        cmd = """python ../../main.py baseanti describe-ip-safety-info  --ip 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_clean_threshold(self):
        cmd = """python ../../main.py baseanti set-clean-threshold  --ip 'xxx' --clean-threshold-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_ip_clean_threshold(self):
        cmd = """python ../../main.py baseanti set-ip-clean-threshold  --ip-clean-threshold-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_clean_threshold_range(self):
        cmd = """python ../../main.py baseanti describe-ip-clean-threshold-range  --ip 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_resource_protect_info(self):
        cmd = """python ../../main.py baseanti describe-ip-resource-protect-info  --ip 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ip_resource_flow(self):
        cmd = """python ../../main.py baseanti describe-ip-resource-flow  --ip 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

