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


class RdsTest(unittest.TestCase):

    def test_describe_accounts(self):
        cmd = """python ../../main.py rds describe-accounts  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_account(self):
        cmd = """python ../../main.py rds create-account  --instance-id 'xxx' --account-name 'xxx' --account-password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_account(self):
        cmd = """python ../../main.py rds delete-account  --instance-id 'xxx' --account-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_grant_privilege(self):
        cmd = """python ../../main.py rds grant-privilege  --instance-id 'xxx' --account-name 'xxx' --account-privileges '[{"":""}]'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_revoke_privilege(self):
        cmd = """python ../../main.py rds revoke-privilege  --instance-id 'xxx' --account-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reset_password(self):
        cmd = """python ../../main.py rds reset-password  --instance-id 'xxx' --account-name 'xxx' --account-password 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_audit(self):
        cmd = """python ../../main.py rds describe-audit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_audit(self):
        cmd = """python ../../main.py rds create-audit  --instance-id 'xxx' --enabled 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_audit(self):
        cmd = """python ../../main.py rds delete-audit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_audit_options(self):
        cmd = """python ../../main.py rds describe-audit-options  --instance-id 'xxx' --name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_audit(self):
        cmd = """python ../../main.py rds modify-audit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_audit_files(self):
        cmd = """python ../../main.py rds describe-audit-files  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_audit_download_url(self):
        cmd = """python ../../main.py rds describe-audit-download-url  --instance-id 'xxx' --file-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_audit(self):
        cmd = """python ../../main.py rds enable-audit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_audit(self):
        cmd = """python ../../main.py rds disable-audit  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_audit_result(self):
        cmd = """python ../../main.py rds describe-audit-result  --instance-id 'xxx' --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_backups(self):
        cmd = """python ../../main.py rds describe-backups  --instance-id 'xxx' --page-number '5' --page-size '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_backup(self):
        cmd = """python ../../main.py rds create-backup """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_backup(self):
        cmd = """python ../../main.py rds delete-backup  --backup-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_backup_download_url(self):
        cmd = """python ../../main.py rds describe-backup-download-url  --backup-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_backup_synchronicities(self):
        cmd = """python ../../main.py rds describe-backup-synchronicities """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_backup_synchronicity(self):
        cmd = """python ../../main.py rds create-backup-synchronicity  --instance-id 'xxx' --dest-region 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_backup_synchronicity(self):
        cmd = """python ../../main.py rds delete-backup-synchronicity  --service-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_binlogs(self):
        cmd = """python ../../main.py rds describe-binlogs  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_binlog_download_url(self):
        cmd = """python ../../main.py rds describe-binlog-download-url  --instance-id 'xxx' --binlog-backup-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_databases(self):
        cmd = """python ../../main.py rds describe-databases  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_database(self):
        cmd = """python ../../main.py rds create-database  --instance-id 'xxx' --db-name 'xxx' --character-set-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_database(self):
        cmd = """python ../../main.py rds delete-database  --instance-id 'xxx' --db-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restore_database_from_backup(self):
        cmd = """python ../../main.py rds restore-database-from-backup  --instance-id 'xxx' --db-name 'xxx' --backup-id 'xxx' --backup-file-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restore_database_from_file(self):
        cmd = """python ../../main.py rds restore-database-from-file  --instance-id 'xxx' --db-name 'xxx' --file-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restore_database_from_oss(self):
        cmd = """python ../../main.py rds restore-database-from-oss  --instance-id 'xxx' --db-name 'xxx' --oss-url 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_error_logs(self):
        cmd = """python ../../main.py rds describe-error-logs  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_import_files(self):
        cmd = """python ../../main.py rds describe-import-files  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_get_upload_key(self):
        cmd = """python ../../main.py rds get-upload-key  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_import_file_shared(self):
        cmd = """python ../../main.py rds set-import-file-shared  --instance-id 'xxx' --file-name 'xxx' --shared 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instances(self):
        cmd = """python ../../main.py rds describe-instances """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instance(self):
        cmd = """python ../../main.py rds create-instance  --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_instance_attributes(self):
        cmd = """python ../../main.py rds describe-instance-attributes  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_instance(self):
        cmd = """python ../../main.py rds delete-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_backup_policy(self):
        cmd = """python ../../main.py rds describe-backup-policy  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_backup_policy(self):
        cmd = """python ../../main.py rds modify-backup-policy  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_name(self):
        cmd = """python ../../main.py rds modify-instance-name  --instance-id 'xxx' --instance-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_failover_instance(self):
        cmd = """python ../../main.py rds failover-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_reboot_instance(self):
        cmd = """python ../../main.py rds reboot-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_enable_internet_access(self):
        cmd = """python ../../main.py rds enable-internet-access  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_disable_internet_access(self):
        cmd = """python ../../main.py rds disable-internet-access  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_restore_instance(self):
        cmd = """python ../../main.py rds restore-instance  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instance_from_backup(self):
        cmd = """python ../../main.py rds create-instance-from-backup  --backup-id 'xxx' --engine 'xxx' --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_instance_spec(self):
        cmd = """python ../../main.py rds modify-instance-spec  --instance-id 'xxx' --new-instance-class 'xxx' --new-instance-storage-gb '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_create_instance_by_time(self):
        cmd = """python ../../main.py rds create-instance-by-time  --instance-id 'xxx' --restore-time 'xxx' --instance-spec '{"":""}'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_connection_mode(self):
        cmd = """python ../../main.py rds modify-connection-mode  --instance-id 'xxx' --connection-mode 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_index_performance(self):
        cmd = """python ../../main.py rds describe-index-performance  --instance-id 'xxx' --query-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_query_performance(self):
        cmd = """python ../../main.py rds describe-query-performance  --instance-id 'xxx' --query-type 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_slow_log_attributes(self):
        cmd = """python ../../main.py rds describe-slow-log-attributes  --instance-id 'xxx' --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_slow_logs(self):
        cmd = """python ../../main.py rds describe-slow-logs  --instance-id 'xxx' --start-time 'xxx' --end-time 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_white_list(self):
        cmd = """python ../../main.py rds describe-white-list  --instance-id 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_modify_white_list(self):
        cmd = """python ../../main.py rds modify-white-list  --instance-id 'xxx' --ips 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

