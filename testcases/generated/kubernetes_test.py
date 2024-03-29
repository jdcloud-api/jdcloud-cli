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


class KubernetesTest(unittest.TestCase):

    def test_describe_node_groups(self):
        cmd = """python ../../main.py kubernetes describe-node-groups """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_node_group(self):
        cmd = """python ../../main.py kubernetes create-node-group  --name 'xxx' --cluster-id 'xxx' --node-config '{"":""}' --initial-node-count '5' --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_node_group(self):
        cmd = """python ../../main.py kubernetes describe-node-group  --node-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_node_group(self):
        cmd = """python ../../main.py kubernetes modify-node-group  --node-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_node_group(self):
        cmd = """python ../../main.py kubernetes delete-node-group  --node-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_node_group_size(self):
        cmd = """python ../../main.py kubernetes set-node-group-size  --node-group-id 'xxx' --expect-count '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_auto_repair(self):
        cmd = """python ../../main.py kubernetes set-auto-repair  --node-group-id 'xxx' --enabled 'true'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_rollback_node_group_upgrade(self):
        cmd = """python ../../main.py kubernetes rollback-node-group-upgrade  --node-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_node_group_ca(self):
        cmd = """python ../../main.py kubernetes set-node-group-ca  --node-group-id 'xxx' --ca-config '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_node_instances(self):
        cmd = """python ../../main.py kubernetes delete-node-instances  --node-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_server_config(self):
        cmd = """python ../../main.py kubernetes describe-server-config """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_versions(self):
        cmd = """python ../../main.py kubernetes describe-versions """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_node_version(self):
        cmd = """python ../../main.py kubernetes describe-node-version  --node-version 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_upgradable_master_versions(self):
        cmd = """python ../../main.py kubernetes describe-upgradable-master-versions  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_upgradable_node_versions(self):
        cmd = """python ../../main.py kubernetes describe-upgradable-node-versions  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_quotas(self):
        cmd = """python ../../main.py kubernetes describe-quotas """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_clusters(self):
        cmd = """python ../../main.py kubernetes describe-clusters """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_cluster(self):
        cmd = """python ../../main.py kubernetes create-cluster  --name 'xxx' --node-group '{"":""}' --master-cidr 'xxx' --access-key 'xxx' --secret-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cluster(self):
        cmd = """python ../../main.py kubernetes describe-cluster  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_cluster(self):
        cmd = """python ../../main.py kubernetes modify-cluster  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_cluster(self):
        cmd = """python ../../main.py kubernetes delete-cluster  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_user_metrics(self):
        cmd = """python ../../main.py kubernetes set-user-metrics  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_abort_upgrade(self):
        cmd = """python ../../main.py kubernetes abort-upgrade  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_progress(self):
        cmd = """python ../../main.py kubernetes describe-progress  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_auto_upgrade(self):
        cmd = """python ../../main.py kubernetes set-auto-upgrade  --cluster-id 'xxx' --auto-upgrade 'true'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_upgrade_cluster(self):
        cmd = """python ../../main.py kubernetes upgrade-cluster  --cluster-id 'xxx' --scope 'xxx' --version 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_addons(self):
        cmd = """python ../../main.py kubernetes set-addons  --cluster-id 'xxx' --addons-config '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

