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


class IpantiTest(unittest.TestCase):

    def test_describe_ddos_attack_logs(self):
        cmd = """python ../../main.py ipanti describe-ddos-attack-logs  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cc_attack_logs(self):
        cmd = """python ../../main.py ipanti describe-cc-attack-logs  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cc_attack_log_details(self):
        cmd = """python ../../main.py ipanti describe-cc-attack-log-details  --start-time 'xxx' --end-time 'xxx' --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_ddos_graph(self):
        cmd = """python ../../main.py ipanti ddos-graph  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_fwd_graph(self):
        cmd = """python ../../main.py ipanti fwd-graph  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_cc_graph(self):
        cmd = """python ../../main.py ipanti cc-graph  --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_forward_rules(self):
        cmd = """python ../../main.py ipanti describe-forward-rules  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_forward_rule(self):
        cmd = """python ../../main.py ipanti create-forward-rule  --instance-id 'xxx' --forward-rule-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_forward_rule(self):
        cmd = """python ../../main.py ipanti describe-forward-rule  --instance-id 'xxx' --forward-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_forward_rule(self):
        cmd = """python ../../main.py ipanti modify-forward-rule  --instance-id 'xxx' --forward-rule-id 'xxx' --forward-rule-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_forward_rule(self):
        cmd = """python ../../main.py ipanti delete-forward-rule  --instance-id 'xxx' --forward-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_switch_forward_rule_protect(self):
        cmd = """python ../../main.py ipanti switch-forward-rule-protect  --instance-id 'xxx' --forward-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_switch_forward_rule_origin(self):
        cmd = """python ../../main.py ipanti switch-forward-rule-origin  --instance-id 'xxx' --forward-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instances(self):
        cmd = """python ../../main.py ipanti describe-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instance(self):
        cmd = """python ../../main.py ipanti create-instance  --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance(self):
        cmd = """python ../../main.py ipanti describe-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_cc(self):
        cmd = """python ../../main.py ipanti modify-instance-cc  --instance-id 'xxx' --c-cspec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_instance_cc(self):
        cmd = """python ../../main.py ipanti enable-instance-cc  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_instance_cc(self):
        cmd = """python ../../main.py ipanti disable-instance-cc  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_url_white_list(self):
        cmd = """python ../../main.py ipanti modify-instance-url-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_instance_url_white_list(self):
        cmd = """python ../../main.py ipanti enable-instance-url-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_instance_url_white_list(self):
        cmd = """python ../../main.py ipanti disable-instance-url-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_name(self):
        cmd = """python ../../main.py ipanti modify-instance-name  --instance-id 'xxx' --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_ip_black_list(self):
        cmd = """python ../../main.py ipanti modify-instance-ip-black-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_instance_ip_black_list(self):
        cmd = """python ../../main.py ipanti enable-instance-ip-black-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_instance_ip_black_list(self):
        cmd = """python ../../main.py ipanti disable-instance-ip-black-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_ip_white_list(self):
        cmd = """python ../../main.py ipanti modify-instance-ip-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_instance_ip_white_list(self):
        cmd = """python ../../main.py ipanti enable-instance-ip-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_instance_ip_white_list(self):
        cmd = """python ../../main.py ipanti disable-instance-ip-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_cc_observer_mode(self):
        cmd = """python ../../main.py ipanti enable-cc-observer-mode  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_cc_observer_mode(self):
        cmd = """python ../../main.py ipanti disable-cc-observer-mode  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_cc_ip_limit(self):
        cmd = """python ../../main.py ipanti enable-cc-ip-limit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_cc_ip_limit(self):
        cmd = """python ../../main.py ipanti disable-cc-ip-limit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_cc_ip_limit(self):
        cmd = """python ../../main.py ipanti set-cc-ip-limit  --instance-id 'xxx' --c-cspec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_web_rules(self):
        cmd = """python ../../main.py ipanti describe-web-rules  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_web_rule(self):
        cmd = """python ../../main.py ipanti create-web-rule  --instance-id 'xxx' --web-rule-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_web_rule(self):
        cmd = """python ../../main.py ipanti describe-web-rule  --instance-id 'xxx' --web-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_web_rule(self):
        cmd = """python ../../main.py ipanti modify-web-rule  --instance-id 'xxx' --web-rule-id 'xxx' --web-rule-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_web_rule(self):
        cmd = """python ../../main.py ipanti delete-web-rule  --instance-id 'xxx' --web-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_switch_web_rule_protect(self):
        cmd = """python ../../main.py ipanti switch-web-rule-protect  --instance-id 'xxx' --web-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_switch_web_rule_origin(self):
        cmd = """python ../../main.py ipanti switch-web-rule-origin  --instance-id 'xxx' --web-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_web_rule_cc(self):
        cmd = """python ../../main.py ipanti enable-web-rule-cc  --instance-id 'xxx' --web-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_web_rule_cc(self):
        cmd = """python ../../main.py ipanti disable-web-rule-cc  --instance-id 'xxx' --web-rule-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

