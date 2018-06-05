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

import unittest
import os
import json


class MonitorTest(unittest.TestCase):

    def test_describe_alarms(self):
        cmd = """python ../../main.py monitor describe-alarms """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_alarm(self):
        cmd = """python ../../main.py monitor create-alarm  --client-token 'xxx' --create-alarm-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_alarms(self):
        cmd = """python ../../main.py monitor delete-alarms  --ids 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_alarms_by_id(self):
        cmd = """python ../../main.py monitor describe-alarms-by-id  --alarm-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_alarm(self):
        cmd = """python ../../main.py monitor update-alarm  --alarm-id 'xxx' --calculation 'xxx' --metric 'xxx' --operation 'xxx' --period '5' --service-code 'xxx' --threshold '' --times '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_alarm(self):
        cmd = """python ../../main.py monitor enable-alarm  --alarm-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_alarm(self):
        cmd = """python ../../main.py monitor disable-alarm  --alarm-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_alarm_history(self):
        cmd = """python ../../main.py monitor describe-alarm-history  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_metrics(self):
        cmd = """python ../../main.py monitor describe-metrics  --service-code 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_metrics_for_create_alarm(self):
        cmd = """python ../../main.py monitor describe-metrics-for-create-alarm """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_metric_data(self):
        cmd = """python ../../main.py monitor describe-metric-data  --metric 'xxx' --service-code 'xxx' --resource-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)
