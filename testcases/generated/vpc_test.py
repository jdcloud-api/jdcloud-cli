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


class VpcTest(unittest.TestCase):

    def test_describe_vpc_peerings(self):
        cmd = """python ../../main.py vpc describe-vpc-peerings """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_vpc_peering(self):
        cmd = """python ../../main.py vpc create-vpc-peering  --vpc-peering-name 'xxx' --vpc-id 'xxx' --remote-vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpc_peering(self):
        cmd = """python ../../main.py vpc describe-vpc-peering  --vpc-peering-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_vpc_peering(self):
        cmd = """python ../../main.py vpc modify-vpc-peering  --vpc-peering-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_vpc_peering(self):
        cmd = """python ../../main.py vpc delete-vpc-peering  --vpc-peering-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_route_tables(self):
        cmd = """python ../../main.py vpc describe-route-tables """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_route_table(self):
        cmd = """python ../../main.py vpc create-route-table  --vpc-id 'xxx' --route-table-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_route_table(self):
        cmd = """python ../../main.py vpc describe-route-table  --route-table-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_route_table(self):
        cmd = """python ../../main.py vpc modify-route-table  --route-table-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_route_table(self):
        cmd = """python ../../main.py vpc delete-route-table  --route-table-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_route_table_rules(self):
        cmd = """python ../../main.py vpc add-route-table-rules  --route-table-id 'xxx' --route-table-rule-specs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_route_table_rules(self):
        cmd = """python ../../main.py vpc remove-route-table-rules  --route-table-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_route_table_rules(self):
        cmd = """python ../../main.py vpc modify-route-table-rules  --route-table-id 'xxx' --modify-route-table-rule-specs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_route_table(self):
        cmd = """python ../../main.py vpc associate-route-table  --route-table-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_route_table(self):
        cmd = """python ../../main.py vpc disassociate-route-table  --route-table-id 'xxx' --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_subnets(self):
        cmd = """python ../../main.py vpc describe-subnets """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_subnet(self):
        cmd = """python ../../main.py vpc create-subnet  --vpc-id 'xxx' --subnet-name 'xxx' --address-prefix 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_subnet(self):
        cmd = """python ../../main.py vpc describe-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_subnet(self):
        cmd = """python ../../main.py vpc modify-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_subnet(self):
        cmd = """python ../../main.py vpc delete-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_acls(self):
        cmd = """python ../../main.py vpc describe-network-acls """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_network_acl(self):
        cmd = """python ../../main.py vpc create-network-acl  --vpc-id 'xxx' --network-acl-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_acl(self):
        cmd = """python ../../main.py vpc describe-network-acl  --network-acl-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_network_acl(self):
        cmd = """python ../../main.py vpc modify-network-acl  --network-acl-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_network_acl(self):
        cmd = """python ../../main.py vpc delete-network-acl  --network-acl-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_network_acl(self):
        cmd = """python ../../main.py vpc associate-network-acl  --network-acl-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_network_acl(self):
        cmd = """python ../../main.py vpc disassociate-network-acl  --network-acl-id 'xxx' --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_network_acl_rules(self):
        cmd = """python ../../main.py vpc add-network-acl-rules  --network-acl-id 'xxx' --network-acl-rule-specs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_network_acl_rules(self):
        cmd = """python ../../main.py vpc remove-network-acl-rules  --network-acl-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_network_acl_rules(self):
        cmd = """python ../../main.py vpc modify-network-acl-rules  --network-acl-id 'xxx' --modify-network-acl-rule-specs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpcs(self):
        cmd = """python ../../main.py vpc describe-vpcs """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_vpc(self):
        cmd = """python ../../main.py vpc create-vpc  --vpc-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpc(self):
        cmd = """python ../../main.py vpc describe-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_vpc(self):
        cmd = """python ../../main.py vpc modify-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_vpc(self):
        cmd = """python ../../main.py vpc delete-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_interfaces(self):
        cmd = """python ../../main.py vpc describe-network-interfaces """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_network_interface(self):
        cmd = """python ../../main.py vpc create-network-interface  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_interface(self):
        cmd = """python ../../main.py vpc describe-network-interface  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_network_interface(self):
        cmd = """python ../../main.py vpc modify-network-interface  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_network_interface(self):
        cmd = """python ../../main.py vpc delete-network-interface  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_elastic_ip(self):
        cmd = """python ../../main.py vpc associate-elastic-ip  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_elastic_ip(self):
        cmd = """python ../../main.py vpc disassociate-elastic-ip  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_assign_secondary_ips(self):
        cmd = """python ../../main.py vpc assign-secondary-ips  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_unassign_secondary_ips(self):
        cmd = """python ../../main.py vpc unassign-secondary-ips  --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_bandwidth_packages(self):
        cmd = """python ../../main.py vpc describe-bandwidth-packages """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_bandwidth_package(self):
        cmd = """python ../../main.py vpc create-bandwidth-package  --name 'xxx' --bandwidth-mbps '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_bandwidth_package(self):
        cmd = """python ../../main.py vpc describe-bandwidth-package  --bandwidth-package-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_bandwidth_package(self):
        cmd = """python ../../main.py vpc modify-bandwidth-package  --bandwidth-package-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_bandwidth_package(self):
        cmd = """python ../../main.py vpc delete-bandwidth-package  --bandwidth-package-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_bandwidth_package_ip(self):
        cmd = """python ../../main.py vpc add-bandwidth-package-ip  --bandwidth-package-id 'xxx' --bandwidth-package-ipspecs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_bandwidth_package_ip(self):
        cmd = """python ../../main.py vpc remove-bandwidth-package-ip  --bandwidth-package-id 'xxx' --bandwidth-package-ipspecs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_bandwidth_package_ip_bandwidth(self):
        cmd = """python ../../main.py vpc modify-bandwidth-package-ip-bandwidth  --bandwidth-package-id 'xxx' --bandwidth-package-ipspecs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_security_groups(self):
        cmd = """python ../../main.py vpc describe-network-security-groups """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_network_security_group(self):
        cmd = """python ../../main.py vpc create-network-security-group  --vpc-id 'xxx' --network-security-group-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_network_security_group(self):
        cmd = """python ../../main.py vpc describe-network-security-group  --network-security-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_network_security_group(self):
        cmd = """python ../../main.py vpc modify-network-security-group  --network-security-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_network_security_group(self):
        cmd = """python ../../main.py vpc delete-network-security-group  --network-security-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_network_security_group_rules(self):
        cmd = """python ../../main.py vpc add-network-security-group-rules  --network-security-group-id 'xxx' --network-security-group-rule-specs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_network_security_group_rules(self):
        cmd = """python ../../main.py vpc remove-network-security-group-rules  --network-security-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_network_security_group_rules(self):
        cmd = """python ../../main.py vpc modify-network-security-group-rules  --network-security-group-id 'xxx' --modify-security-group-rule-specs '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_quota(self):
        cmd = """python ../../main.py vpc describe-quota  --type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ips(self):
        cmd = """python ../../main.py vpc describe-elastic-ips """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_elastic_ips(self):
        cmd = """python ../../main.py vpc create-elastic-ips  --max-count '5' --elastic-ip-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ip(self):
        cmd = """python ../../main.py vpc describe-elastic-ip  --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_elastic_ip(self):
        cmd = """python ../../main.py vpc modify-elastic-ip  --elastic-ip-id 'xxx' --bandwidth-mbps '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_elastic_ip(self):
        cmd = """python ../../main.py vpc delete-elastic-ip  --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_edge_ip_providers(self):
        cmd = """python ../../main.py vpc describe-edge-ip-providers """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

