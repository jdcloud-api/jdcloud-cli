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


class VmTest(unittest.TestCase):

    def test_describe_image(self):
        cmd = """python ../../main.py vm describe-image  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_image(self):
        cmd = """python ../../main.py vm delete-image  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_images(self):
        cmd = """python ../../main.py vm describe-images """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_image_constraints(self):
        cmd = """python ../../main.py vm describe-image-constraints  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_image_constraints_batch(self):
        cmd = """python ../../main.py vm describe-image-constraints-batch """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_share_image(self):
        cmd = """python ../../main.py vm share-image  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_un_share_image(self):
        cmd = """python ../../main.py vm un-share-image  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_release_image(self):
        cmd = """python ../../main.py vm release-image  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_un_release_image(self):
        cmd = """python ../../main.py vm un-release-image  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_image_members(self):
        cmd = """python ../../main.py vm describe-image-members  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_copy_images(self):
        cmd = """python ../../main.py vm copy-images  --destination-region 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_image_attribute(self):
        cmd = """python ../../main.py vm modify-image-attribute  --image-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_import_image(self):
        cmd = """python ../../main.py vm import-image  --architecture 'xxx' --os-type 'xxx' --platform 'xxx' --disk-format 'xxx' --system-disk-size-gb '5' --image-url 'xxx' --image-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_export_image(self):
        cmd = """python ../../main.py vm export-image  --image-id 'xxx' --role-name 'xxx' --oss-url 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_image_tasks(self):
        cmd = """python ../../main.py vm image-tasks  --task-action 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instances(self):
        cmd = """python ../../main.py vm describe-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instances(self):
        cmd = """python ../../main.py vm create-instances  --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance(self):
        cmd = """python ../../main.py vm describe-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_instance(self):
        cmd = """python ../../main.py vm delete-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_status(self):
        cmd = """python ../../main.py vm describe-instance-status """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_private_ip_address(self):
        cmd = """python ../../main.py vm describe-instance-private-ip-address """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_instance(self):
        cmd = """python ../../main.py vm stop-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_instance(self):
        cmd = """python ../../main.py vm start-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reboot_instance(self):
        cmd = """python ../../main.py vm reboot-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_attach_network_interface(self):
        cmd = """python ../../main.py vm attach-network-interface  --instance-id 'xxx' --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_detach_network_interface(self):
        cmd = """python ../../main.py vm detach-network-interface  --instance-id 'xxx' --network-interface-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_network_attribute(self):
        cmd = """python ../../main.py vm modify-instance-network-attribute  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_associate_elastic_ip(self):
        cmd = """python ../../main.py vm associate-elastic-ip  --instance-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disassociate_elastic_ip(self):
        cmd = """python ../../main.py vm disassociate-elastic-ip  --instance-id 'xxx' --elastic-ip-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_image(self):
        cmd = """python ../../main.py vm create-image  --instance-id 'xxx' --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_attach_disk(self):
        cmd = """python ../../main.py vm attach-disk  --instance-id 'xxx' --disk-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_detach_disk(self):
        cmd = """python ../../main.py vm detach-disk  --instance-id 'xxx' --disk-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_disk_attribute(self):
        cmd = """python ../../main.py vm modify-instance-disk-attribute  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_attribute(self):
        cmd = """python ../../main.py vm modify-instance-attribute  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_password(self):
        cmd = """python ../../main.py vm modify-instance-password  --instance-id 'xxx' --password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_vnc_url(self):
        cmd = """python ../../main.py vm describe-instance-vnc-url  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_resize_instance(self):
        cmd = """python ../../main.py vm resize-instance  --instance-id 'xxx' --instance-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_rebuild_instance(self):
        cmd = """python ../../main.py vm rebuild-instance  --instance-id 'xxx' --password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_templates(self):
        cmd = """python ../../main.py vm describe-instance-templates """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instance_template(self):
        cmd = """python ../../main.py vm create-instance-template  --instance-template-data '{"":""}' --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_template(self):
        cmd = """python ../../main.py vm describe-instance-template  --instance-template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_update_instance_template(self):
        cmd = """python ../../main.py vm update-instance-template  --instance-template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_instance_template(self):
        cmd = """python ../../main.py vm delete-instance-template  --instance-template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_verify_instance_template(self):
        cmd = """python ../../main.py vm verify-instance-template  --instance-template-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_types(self):
        cmd = """python ../../main.py vm describe-instance-types """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_keypairs(self):
        cmd = """python ../../main.py vm describe-keypairs """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_keypair(self):
        cmd = """python ../../main.py vm create-keypair  --key-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_import_keypair(self):
        cmd = """python ../../main.py vm import-keypair  --key-name 'xxx' --public-key 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_keypair(self):
        cmd = """python ../../main.py vm delete-keypair  --key-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_quotas(self):
        cmd = """python ../../main.py vm describe-quotas """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

