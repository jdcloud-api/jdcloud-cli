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


class JmrTest(unittest.TestCase):

    def test_create_cluster_in_new_network(self):
        cmd = """python ../../main.py jmr create-cluster-in-new-network  --cluster-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_show_cluster_details(self):
        cmd = """python ../../main.py jmr show-cluster-details  --id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_release_cluster(self):
        cmd = """python ../../main.py jmr release-cluster  --id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_key(self):
        cmd = """python ../../main.py jmr get-key """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_property_value(self):
        cmd = """python ../../main.py jmr get-property-value """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_hardware_stack(self):
        cmd = """python ../../main.py jmr get-hardware-stack """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_instance_list(self):
        cmd = """python ../../main.py jmr get-instance-list """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_idata_cluster(self):
        cmd = """python ../../main.py jmr idata-cluster  --id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_software_info(self):
        cmd = """python ../../main.py jmr get-software-info  --ver 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_software_and_version_info(self):
        cmd = """python ../../main.py jmr get-software-and-version-info  --ver 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_jmr_version_list(self):
        cmd = """python ../../main.py jmr get-jmr-version-list """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_calculate_cluster_price(self):
        cmd = """python ../../main.py jmr calculate-cluster-price  --cluster-list-view-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_avaliable_num(self):
        cmd = """python ../../main.py jmr get-avaliable-num """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_server_quota(self):
        cmd = """python ../../main.py jmr query-server-quota """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_vpcs(self):
        cmd = """python ../../main.py jmr query-vpcs """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_vpc_subnets(self):
        cmd = """python ../../main.py jmr query-vpc-subnets  --vpc-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_cluster(self):
        cmd = """python ../../main.py jmr delete-cluster  --record-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_floating_ip(self):
        cmd = """python ../../main.py jmr query-floating-ip  --record-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_validate_user(self):
        cmd = """python ../../main.py jmr validate-user """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_renew_billing_order(self):
        cmd = """python ../../main.py jmr renew-billing-order  --cluster-id 'xxx' --type '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_validate_name(self):
        cmd = """python ../../main.py jmr validate-name  --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_access_keys(self):
        cmd = """python ../../main.py jmr get-access-keys """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_cluster_expansion(self):
        cmd = """python ../../main.py jmr cluster-expansion  --cluster-id 'xxx' --expansion-num '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_calculate_expansion_price(self):
        cmd = """python ../../main.py jmr calculate-expansion-price  --cluster-id 'xxx' --expansion-num '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cluster_detail_info(self):
        cmd = """python ../../main.py jmr get-cluster-detail-info  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_monitor_service_list(self):
        cmd = """python ../../main.py jmr monitor-service-list  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_monitor_details(self):
        cmd = """python ../../main.py jmr monitor-details  --cluster-id 'xxx' --service 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_first_server_vnc_url(self):
        cmd = """python ../../main.py jmr get-first-server-vnc-url  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_job_type_list(self):
        cmd = """python ../../main.py jmr get-job-type-list  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_job_list(self):
        cmd = """python ../../main.py jmr get-job-list  --jmr-job-view-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_is_valid_job_name(self):
        cmd = """python ../../main.py jmr is-valid-job-name  --job-id 'xxx' --job-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_job(self):
        cmd = """python ../../main.py jmr create-job  --jmr-job-view-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_job(self):
        cmd = """python ../../main.py jmr modify-job  --jmr-job-view-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_job(self):
        cmd = """python ../../main.py jmr delete-job  --job-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_and_excute_job(self):
        cmd = """python ../../main.py jmr create-and-excute-job  --jmr-job-view-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_execute_job(self):
        cmd = """python ../../main.py jmr execute-job  --jmr-task-view-model '{"":""}' --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_show_job_details(self):
        cmd = """python ../../main.py jmr show-job-details  --job-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_task_list(self):
        cmd = """python ../../main.py jmr get-task-list  --job-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_hdfs_file(self):
        cmd = """python ../../main.py jmr delete-hdfs-file  --cluster-id 'xxx' --file-path 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cluster_job_count(self):
        cmd = """python ../../main.py jmr get-cluster-job-count  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cluster_cron_job_count(self):
        cmd = """python ../../main.py jmr get-cluster-cron-job-count  --cluster-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cron_job_list(self):
        cmd = """python ../../main.py jmr get-cron-job-list  --jmr-plan-view-model '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_is_valid_plan_name(self):
        cmd = """python ../../main.py jmr is-valid-plan-name  --plan-id 'xxx' --plan-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_cron_job(self):
        cmd = """python ../../main.py jmr create-cron-job  --jmr-plan-view-model '{"":""}' --time 'xxx' --month 'xxx' --week 'xxx' --day 'xxx' --hour 'xxx' --minute 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cron_job_detail(self):
        cmd = """python ../../main.py jmr get-cron-job-detail  --plan-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_cron_job(self):
        cmd = """python ../../main.py jmr modify-cron-job  --jmr-plan-view-model '{"":""}' --time 'xxx' --month 'xxx' --week 'xxx' --day 'xxx' --hour 'xxx' --minute 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_pause_cron_job(self):
        cmd = """python ../../main.py jmr pause-cron-job  --plan-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_resume_cron_job(self):
        cmd = """python ../../main.py jmr resume-cron-job  --plan-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_cron_job(self):
        cmd = """python ../../main.py jmr delete-cron-job  --plan-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cron_job_task_list(self):
        cmd = """python ../../main.py jmr get-cron-job-task-list  --plan-id '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_cron_job_task_list_by_job_id(self):
        cmd = """python ../../main.py jmr get-cron-job-task-list-by-job-id  --job-id 'xxx' --plan-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_run_cron_job_once(self):
        cmd = """python ../../main.py jmr run-cron-job-once  --plan-id '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_last_cron_job_task(self):
        cmd = """python ../../main.py jmr get-last-cron-job-task  --job-id 'xxx' --plan-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_query_executing_job_list(self):
        cmd = """python ../../main.py jmr query-executing-job-list """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_work_flow_list(self):
        cmd = """python ../../main.py jmr get-work-flow-list  --workflow-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_save_work_flow(self):
        cmd = """python ../../main.py jmr save-work-flow  --workflow '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_work_flow(self):
        cmd = """python ../../main.py jmr delete-work-flow  --workflow-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_run_work_flow(self):
        cmd = """python ../../main.py jmr run-work-flow  --workflow-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_wf_instance_detail(self):
        cmd = """python ../../main.py jmr wf-instance-detail  --wf-instance-id 'xxx' --wf-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_work_flow_tracker_list(self):
        cmd = """python ../../main.py jmr get-work-flow-tracker-list """
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_work_flow_tracker(self):
        cmd = """python ../../main.py jmr delete-work-flow-tracker  --tracker-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print content
        result = json.loads(content)
        self.assertIsInstance(result, dict)

