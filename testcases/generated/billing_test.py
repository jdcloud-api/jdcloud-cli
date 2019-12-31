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


class BillingTest(unittest.TestCase):

    def test_query_bill_summary(self):
        cmd = """python ../../main.py billing query-bill-summary  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_bill_detail(self):
        cmd = """python ../../main.py billing query-bill-detail  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_calculate_total_price(self):
        cmd = """python ../../main.py billing calculate-total-price  --cmd '5' --package-count '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

