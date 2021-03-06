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


class YundingTest(unittest.TestCase):

    def test_assign_secondary_ips(self):
        cmd = """python ../../main.py yunding assign-secondary-ips  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_unassign_secondary_ips(self):
        cmd = """python ../../main.py yunding unassign-secondary-ips  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_rds_instances(self):
        cmd = """python ../../main.py yunding describe-rds-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_rds_instance(self):
        cmd = """python ../../main.py yunding describe-rds-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_info(self):
        cmd = """python ../../main.py yunding describe-instance-info  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_rds_white_list(self):
        cmd = """python ../../main.py yunding describe-rds-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_rds_white_list(self):
        cmd = """python ../../main.py yunding modify-rds-white-list  --instance-id 'xxx' --ips 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_rds_accounts(self):
        cmd = """python ../../main.py yunding describe-rds-accounts  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_rds_account(self):
        cmd = """python ../../main.py yunding create-rds-account  --instance-id 'xxx' --account-name 'xxx' --account-password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_rds_account(self):
        cmd = """python ../../main.py yunding delete-rds-account  --instance-id 'xxx' --account-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_grant_rds_privilege(self):
        cmd = """python ../../main.py yunding grant-rds-privilege  --instance-id 'xxx' --account-name 'xxx' --account-privileges '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_rds_databases(self):
        cmd = """python ../../main.py yunding describe-rds-databases  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_rds_database(self):
        cmd = """python ../../main.py yunding create-rds-database  --instance-id 'xxx' --db-name 'xxx' --character-set-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_rds_database(self):
        cmd = """python ../../main.py yunding delete-rds-database  --instance-id 'xxx' --db-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_yd_rds_instances(self):
        cmd = """python ../../main.py yunding describe-yd-rds-instances  --app-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

