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


class CpsTest(unittest.TestCase):

    def test_describe_ipv6address(self):
        cmd = """python ../../main.py cps describe-ipv6address  --ipv6address-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ipv6addresses(self):
        cmd = """python ../../main.py cps describe-ipv6addresses """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_assign_ipv6addresses_bandwidth(self):
        cmd = """python ../../main.py cps assign-ipv6addresses-bandwidth  --ipv6address-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_ipv6address_bandwidth(self):
        cmd = """python ../../main.py cps modify-ipv6address-bandwidth  --ipv6address-id 'xxx' --bandwidth '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_certs(self):
        cmd = """python ../../main.py cps describe-certs """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_cert(self):
        cmd = """python ../../main.py cps create-cert  --cert-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cert(self):
        cmd = """python ../../main.py cps describe-cert  --cert-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_cert(self):
        cmd = """python ../../main.py cps remove-cert  --cert-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_cert(self):
        cmd = """python ../../main.py cps modify-cert  --cert-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_alias_ips(self):
        cmd = """python ../../main.py cps describe-alias-ips """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_alias_ip(self):
        cmd = """python ../../main.py cps create-alias-ip  --alias-ip-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_alias_ip(self):
        cmd = """python ../../main.py cps delete-alias-ip  --alias-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_secondary_cidrs(self):
        cmd = """python ../../main.py cps describe-secondary-cidrs  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_secondary_cidr(self):
        cmd = """python ../../main.py cps create-secondary-cidr  --secondary-cidr-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_secondary_cidr(self):
        cmd = """python ../../main.py cps delete-secondary-cidr  --secondary-cidr-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ips(self):
        cmd = """python ../../main.py cps describe-elastic-ips """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_apply_elastic_ips(self):
        cmd = """python ../../main.py cps apply-elastic-ips  --elastic-ip-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ip(self):
        cmd = """python ../../main.py cps describe-elastic-ip  --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_elastic_ip_bandwidth(self):
        cmd = """python ../../main.py cps modify-elastic-ip-bandwidth  --elastic-ip-id 'xxx' --bandwidth '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_elastic_ip_name(self):
        cmd = """python ../../main.py cps describe-elastic-ip-name  --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_server_groups(self):
        cmd = """python ../../main.py cps describe-server-groups """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_server_group(self):
        cmd = """python ../../main.py cps create-server-group  --server-group-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_server_group(self):
        cmd = """python ../../main.py cps describe-server-group  --server-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_server_group(self):
        cmd = """python ../../main.py cps modify-server-group  --server-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_server_group(self):
        cmd = """python ../../main.py cps delete-server-group  --server-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_keypairs(self):
        cmd = """python ../../main.py cps describe-keypairs """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_keypairs(self):
        cmd = """python ../../main.py cps create-keypairs  --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_import_keypairs(self):
        cmd = """python ../../main.py cps import-keypairs  --name 'xxx' --public-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_keypair(self):
        cmd = """python ../../main.py cps describe-keypair  --keypair-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_keypairs(self):
        cmd = """python ../../main.py cps delete-keypairs  --keypair-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_load_balancers(self):
        cmd = """python ../../main.py cps describe-load-balancers """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_load_balancer(self):
        cmd = """python ../../main.py cps create-load-balancer  --load-balancer-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_load_balancer(self):
        cmd = """python ../../main.py cps modify-load-balancer  --load-balancer-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_load_balancer(self):
        cmd = """python ../../main.py cps describe-load-balancer  --load-balancer-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_load_balancer(self):
        cmd = """python ../../main.py cps start-load-balancer  --load-balancer-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_load_balancer(self):
        cmd = """python ../../main.py cps stop-load-balancer  --load-balancer-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_elastic_ip_lb(self):
        cmd = """python ../../main.py cps associate-elastic-ip-lb  --load-balancer-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_elastic_ip_lb(self):
        cmd = """python ../../main.py cps disassociate-elastic-ip-lb  --load-balancer-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_slbs_name(self):
        cmd = """python ../../main.py cps describe-slbs-name  --load-balancer-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_servers(self):
        cmd = """python ../../main.py cps describe-servers  --server-group-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_servers(self):
        cmd = """python ../../main.py cps add-servers  --server-group-id 'xxx' --server-spec '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_server(self):
        cmd = """python ../../main.py cps modify-server  --server-group-id 'xxx' --server-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_remove_server(self):
        cmd = """python ../../main.py cps remove-server  --server-group-id 'xxx' --server-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ipv6gateways(self):
        cmd = """python ../../main.py cps describe-ipv6gateways """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_ipv6gateway(self):
        cmd = """python ../../main.py cps describe-ipv6gateway  --ipv6gateway-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_ipv6gateway(self):
        cmd = """python ../../main.py cps modify-ipv6gateway  --ipv6gateway-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_basic_subnet(self):
        cmd = """python ../../main.py cps describe-basic-subnet  --az 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_subnets(self):
        cmd = """python ../../main.py cps describe-subnets """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_subnet(self):
        cmd = """python ../../main.py cps create-subnet  --subnet-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_assign_ipv6cidr(self):
        cmd = """python ../../main.py cps assign-ipv6cidr  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_subnet(self):
        cmd = """python ../../main.py cps describe-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_subnet(self):
        cmd = """python ../../main.py cps modify-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_subnet(self):
        cmd = """python ../../main.py cps delete-subnet  --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpc(self):
        cmd = """python ../../main.py cps describe-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_vpc(self):
        cmd = """python ../../main.py cps modify-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_vpc(self):
        cmd = """python ../../main.py cps delete-vpc  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_vpcs(self):
        cmd = """python ../../main.py cps describe-vpcs """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_vpc(self):
        cmd = """python ../../main.py cps create-vpc  --vpc-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_assign_ipv6gateway(self):
        cmd = """python ../../main.py cps assign-ipv6gateway  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_listeners(self):
        cmd = """python ../../main.py cps describe-listeners """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_listener(self):
        cmd = """python ../../main.py cps create-listener  --listener-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_listener(self):
        cmd = """python ../../main.py cps modify-listener  --listener-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_listener(self):
        cmd = """python ../../main.py cps describe-listener  --listener-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_listener(self):
        cmd = """python ../../main.py cps delete-listener  --listener-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_listener(self):
        cmd = """python ../../main.py cps start-listener  --listener-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_listener(self):
        cmd = """python ../../main.py cps stop-listener  --listener-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_device_types(self):
        cmd = """python ../../main.py cps describe-device-types """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_os(self):
        cmd = """python ../../main.py cps describe-os  --device-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_device_raids(self):
        cmd = """python ../../main.py cps describe-device-raids  --device-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance(self):
        cmd = """python ../../main.py cps describe-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instances(self):
        cmd = """python ../../main.py cps describe-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instances(self):
        cmd = """python ../../main.py cps create-instances  --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_name(self):
        cmd = """python ../../main.py cps describe-instance-name  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_assign_ipv6address(self):
        cmd = """python ../../main.py cps assign-ipv6address  --instance-id 'xxx' --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance(self):
        cmd = """python ../../main.py cps modify-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_raid(self):
        cmd = """python ../../main.py cps describe-instance-raid  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_status(self):
        cmd = """python ../../main.py cps describe-instance-status  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restart_instance(self):
        cmd = """python ../../main.py cps restart-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_instance(self):
        cmd = """python ../../main.py cps stop-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_instance(self):
        cmd = """python ../../main.py cps start-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restart_instances(self):
        cmd = """python ../../main.py cps restart-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_instances(self):
        cmd = """python ../../main.py cps stop-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_instances(self):
        cmd = """python ../../main.py cps start-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reinstall_instance(self):
        cmd = """python ../../main.py cps reinstall-instance  --instance-id 'xxx' --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_bandwidth(self):
        cmd = """python ../../main.py cps modify-bandwidth  --instance-id 'xxx' --bandwidth '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_elastic_ip(self):
        cmd = """python ../../main.py cps associate-elastic-ip  --instance-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_elastic_ip(self):
        cmd = """python ../../main.py cps disassociate-elastic-ip  --instance-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reset_password(self):
        cmd = """python ../../main.py cps reset-password  --instance-id 'xxx' --password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_available_private_ip(self):
        cmd = """python ../../main.py cps describe-available-private-ip  --instance-id 'xxx' --subnet-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_monitor_info(self):
        cmd = """python ../../main.py cps describe-instance-monitor-info  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_event_logs(self):
        cmd = """python ../../main.py cps describe-event-logs  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_route_table(self):
        cmd = """python ../../main.py cps describe-route-table  --route-table-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_route_tables(self):
        cmd = """python ../../main.py cps describe-route-tables """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_regiones(self):
        cmd = """python ../../main.py cps describe-regiones """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_cpslbregions(self):
        cmd = """python ../../main.py cps describe-cpslbregions """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

