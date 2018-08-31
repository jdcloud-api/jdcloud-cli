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


class MongodbTest(unittest.TestCase):

    def test_describe_instances(self):
        cmd = """python ../../main.py mongodb describe-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instance(self):
        cmd = """python ../../main.py mongodb create-instance  --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_instance(self):
        cmd = """python ../../main.py mongodb delete-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reset_password(self):
        cmd = """python ../../main.py mongodb reset-password  --instance-id 'xxx' --account-password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_spec(self):
        cmd = """python ../../main.py mongodb modify-instance-spec  --instance-id 'xxx' --instance-class 'xxx' --instance-storage-gb '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_name(self):
        cmd = """python ../../main.py mongodb modify-instance-name  --instance-id 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_backup_policy(self):
        cmd = """python ../../main.py mongodb describe-backup-policy  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_backup_policy(self):
        cmd = """python ../../main.py mongodb modify-backup-policy  --instance-id 'xxx' --preferred-backup-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restore_instance(self):
        cmd = """python ../../main.py mongodb restore-instance  --instance-id 'xxx' --backup-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_flavors(self):
        cmd = """python ../../main.py mongodb describe-flavors """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_available_zones(self):
        cmd = """python ../../main.py mongodb describe-available-zones """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_backups(self):
        cmd = """python ../../main.py mongodb describe-backups """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_backup(self):
        cmd = """python ../../main.py mongodb create-backup  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_backup(self):
        cmd = """python ../../main.py mongodb delete-backup  --backup-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_backup_download_url(self):
        cmd = """python ../../main.py mongodb backup-download-url  --backup-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_security_ips(self):
        cmd = """python ../../main.py mongodb describe-security-ips  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_security_ips(self):
        cmd = """python ../../main.py mongodb modify-security-ips  --instance-id 'xxx' --modify-mode 'xxx' --security-ips 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

