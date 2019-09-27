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


class IamTest(unittest.TestCase):

    def test_enable_sub_user_access_key(self):
        cmd = """python ../../main.py iam enable-sub-user-access-key  --sub-user 'xxx' --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_sub_user_access_key(self):
        cmd = """python ../../main.py iam disable-sub-user-access-key  --sub-user 'xxx' --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_sub_user_access_key(self):
        cmd = """python ../../main.py iam delete-sub-user-access-key  --sub-user 'xxx' --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_group(self):
        cmd = """python ../../main.py iam create-group  --create-group-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_group(self):
        cmd = """python ../../main.py iam describe-group  --group-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_group(self):
        cmd = """python ../../main.py iam update-group  --group-name 'xxx' --update-group-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_group(self):
        cmd = """python ../../main.py iam delete-group  --group-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_group_sub_users(self):
        cmd = """python ../../main.py iam describe-group-sub-users  --group-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_groups(self):
        cmd = """python ../../main.py iam describe-groups """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_attached_group_policies(self):
        cmd = """python ../../main.py iam describe-attached-group-policies  --group-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_detach_group_policy(self):
        cmd = """python ../../main.py iam detach-group-policy  --group-name 'xxx' --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_attach_group_policy(self):
        cmd = """python ../../main.py iam attach-group-policy  --group-name 'xxx' --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_sub_user_from_group(self):
        cmd = """python ../../main.py iam remove-sub-user-from-group  --group-name 'xxx' --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_sub_user_to_group(self):
        cmd = """python ../../main.py iam add-sub-user-to-group  --group-name 'xxx' --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_permission(self):
        cmd = """python ../../main.py iam create-permission  --create-permission-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_permission_detail(self):
        cmd = """python ../../main.py iam describe-permission-detail  --permission-id '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_permission(self):
        cmd = """python ../../main.py iam update-permission  --permission-id '5' --update-permission-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_permissions(self):
        cmd = """python ../../main.py iam describe-permissions  --page-number '5' --page-size '5' --query-type '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_sub_user_permissions(self):
        cmd = """python ../../main.py iam describe-sub-user-permissions  --sub-user 'xxx' --page-number '5' --page-size '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_permissions_to_sub_user(self):
        cmd = """python ../../main.py iam add-permissions-to-sub-user  --sub-user 'xxx' --add-permissions-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_permission_of_sub_user(self):
        cmd = """python ../../main.py iam remove-permission-of-sub-user  --permission-id '5' --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_policy(self):
        cmd = """python ../../main.py iam create-policy  --create-policy-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_policy(self):
        cmd = """python ../../main.py iam describe-policy  --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_policy(self):
        cmd = """python ../../main.py iam delete-policy  --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_policy_description(self):
        cmd = """python ../../main.py iam update-policy-description  --policy-name 'xxx' --update-policy-description-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_policies(self):
        cmd = """python ../../main.py iam describe-policies """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_role(self):
        cmd = """python ../../main.py iam create-role  --create-role-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_role(self):
        cmd = """python ../../main.py iam describe-role  --role-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_role(self):
        cmd = """python ../../main.py iam delete-role  --role-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_assume_role_policy(self):
        cmd = """python ../../main.py iam update-assume-role-policy  --role-name 'xxx' --update-assume-role-policy-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_roles(self):
        cmd = """python ../../main.py iam describe-roles """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_attach_role_policy(self):
        cmd = """python ../../main.py iam attach-role-policy  --role-name 'xxx' --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_detach_role_policy(self):
        cmd = """python ../../main.py iam detach-role-policy  --role-name 'xxx' --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_role_policies(self):
        cmd = """python ../../main.py iam describe-role-policies  --role-name 'xxx' --sort '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_sub_user(self):
        cmd = """python ../../main.py iam create-sub-user  --create-sub-user-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_sub_user(self):
        cmd = """python ../../main.py iam describe-sub-user  --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_sub_user(self):
        cmd = """python ../../main.py iam update-sub-user  --sub-user 'xxx' --update-sub-user-info '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_sub_user(self):
        cmd = """python ../../main.py iam delete-sub-user  --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_sub_users(self):
        cmd = """python ../../main.py iam describe-sub-users """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_sub_user_groups(self):
        cmd = """python ../../main.py iam describe-sub-user-groups  --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_attached_sub_user_policies(self):
        cmd = """python ../../main.py iam describe-attached-sub-user-policies  --sub-user 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_detach_sub_user_policy(self):
        cmd = """python ../../main.py iam detach-sub-user-policy  --sub-user 'xxx' --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_attach_sub_user_policy(self):
        cmd = """python ../../main.py iam attach-sub-user-policy  --sub-user 'xxx' --policy-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_user_access_keys(self):
        cmd = """python ../../main.py iam describe-user-access-keys """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_user_access_key(self):
        cmd = """python ../../main.py iam create-user-access-key """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enabled_user_access_key(self):
        cmd = """python ../../main.py iam enabled-user-access-key  --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disabled_user_access_key(self):
        cmd = """python ../../main.py iam disabled-user-access-key  --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_user_access_key(self):
        cmd = """python ../../main.py iam delete-user-access-key  --access-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

