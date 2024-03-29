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


class PodTest(unittest.TestCase):

    def test_describe_secrets(self):
        cmd = """python ../../main.py pod describe-secrets """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_secret(self):
        cmd = """python ../../main.py pod create-secret  --name 'xxx' --secret-type 'xxx' --data '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_secret(self):
        cmd = """python ../../main.py pod describe-secret  --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_secret(self):
        cmd = """python ../../main.py pod delete-secret  --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_config_file(self):
        cmd = """python ../../main.py pod create-config-file  --name 'xxx' --data '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_config_file(self):
        cmd = """python ../../main.py pod describe-config-file  --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_config_file(self):
        cmd = """python ../../main.py pod delete-config-file  --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_config_file(self):
        cmd = """python ../../main.py pod update-config-file  --name 'xxx' --name 'xxx' --data '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_quota(self):
        cmd = """python ../../main.py pod describe-quota  --resource-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_container(self):
        cmd = """python ../../main.py pod describe-container  --pod-id 'xxx' --container-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_exec_create(self):
        cmd = """python ../../main.py pod exec-create  --pod-id 'xxx' --container-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_exec_get_exit_code(self):
        cmd = """python ../../main.py pod exec-get-exit-code  --pod-id 'xxx' --container-name 'xxx' --exec-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_resize_tty(self):
        cmd = """python ../../main.py pod resize-tty  --pod-id 'xxx' --container-name 'xxx' --height '5' --width '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_pods(self):
        cmd = """python ../../main.py pod describe-pods """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_pods(self):
        cmd = """python ../../main.py pod create-pods  --pod-spec '{"":""}' --max-count '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_check_pod_name(self):
        cmd = """python ../../main.py pod check-pod-name  --pod-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_pod(self):
        cmd = """python ../../main.py pod describe-pod  --pod-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_pod(self):
        cmd = """python ../../main.py pod delete-pod  --pod-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_pod(self):
        cmd = """python ../../main.py pod start-pod  --pod-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_pod(self):
        cmd = """python ../../main.py pod stop-pod  --pod-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_pod_attribute(self):
        cmd = """python ../../main.py pod modify-pod-attribute  --pod-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_elastic_ip(self):
        cmd = """python ../../main.py pod associate-elastic-ip  --pod-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_elastic_ip(self):
        cmd = """python ../../main.py pod disassociate-elastic-ip  --pod-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_container_logs(self):
        cmd = """python ../../main.py pod get-container-logs  --pod-id 'xxx' --container-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_rebuild_pod(self):
        cmd = """python ../../main.py pod rebuild-pod  --pod-id 'xxx' --containers '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_resize_pod(self):
        cmd = """python ../../main.py pod resize-pod  --pod-id 'xxx' --instance-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_types(self):
        cmd = """python ../../main.py pod describe-instance-types """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

