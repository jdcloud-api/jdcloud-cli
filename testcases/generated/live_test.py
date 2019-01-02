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


class LiveTest(unittest.TestCase):

    def test_describe_live_app(self):
        cmd = """python ../../main.py live describe-live-app """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_app(self):
        cmd = """python ../../main.py live add-live-app  --publish-domain 'xxx' --app-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_live_app(self):
        cmd = """python ../../main.py live start-live-app  --publish-domain 'xxx' --app-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_live_app(self):
        cmd = """python ../../main.py live stop-live-app  --publish-domain 'xxx' --app-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_app(self):
        cmd = """python ../../main.py live delete-live-app  --publish-domain 'xxx' --app-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_domain(self):
        cmd = """python ../../main.py live add-live-domain  --publish-domain 'xxx' --play-domain 'xxx' --region 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_start_live_domain(self):
        cmd = """python ../../main.py live start-live-domain  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_stop_live_domain(self):
        cmd = """python ../../main.py live stop-live-domain  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_live_domain_detail(self):
        cmd = """python ../../main.py live describe-live-domain-detail  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_domain(self):
        cmd = """python ../../main.py live delete-live-domain  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_record_templates(self):
        cmd = """python ../../main.py live describe-custom-live-stream-record-templates """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_custom_live_stream_record_template(self):
        cmd = """python ../../main.py live add-custom-live-stream-record-template  --record-period '5' --save-bucket 'xxx' --save-endpoint 'xxx' --record-file-type 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_app_record(self):
        cmd = """python ../../main.py live add-live-stream-app-record  --app-name 'xxx' --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_domain_record(self):
        cmd = """python ../../main.py live add-live-stream-domain-record  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_record_config(self):
        cmd = """python ../../main.py live describe-custom-live-stream-record-config """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_live_stream_record_notify_config(self):
        cmd = """python ../../main.py live set-live-stream-record-notify-config  --publish-domain 'xxx' --notify-url 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_custom_live_stream_record_template(self):
        cmd = """python ../../main.py live delete-custom-live-stream-record-template  --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_app_record(self):
        cmd = """python ../../main.py live delete-live-stream-app-record  --publish-domain 'xxx' --app-name 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_domain_record(self):
        cmd = """python ../../main.py live delete-live-stream-domain-record  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_live_stream_record_notify_config(self):
        cmd = """python ../../main.py live describe-live-stream-record-notify-config  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_record_notify_config(self):
        cmd = """python ../../main.py live delete-live-stream-record-notify-config  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_custom_live_stream_snapshot_template(self):
        cmd = """python ../../main.py live add-custom-live-stream-snapshot-template  --format 'xxx' --width '5' --height '5' --fill-type '5' --snapshot-interval '5' --save-mode '5' --save-bucket 'xxx' --save-endpoint 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_snapshot_config(self):
        cmd = """python ../../main.py live describe-custom-live-stream-snapshot-config """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_snapshot_templates(self):
        cmd = """python ../../main.py live describe-custom-live-stream-snapshot-templates """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_app_snapshot(self):
        cmd = """python ../../main.py live add-live-stream-app-snapshot  --app-name 'xxx' --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_domain_snapshot(self):
        cmd = """python ../../main.py live add-live-stream-domain-snapshot  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_live_stream_snapshot_notify_config(self):
        cmd = """python ../../main.py live set-live-stream-snapshot-notify-config  --publish-domain 'xxx' --notify-url 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_custom_live_stream_snapshot_template(self):
        cmd = """python ../../main.py live delete-custom-live-stream-snapshot-template  --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_app_snapshot(self):
        cmd = """python ../../main.py live delete-live-stream-app-snapshot  --publish-domain 'xxx' --app-name 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_domain_snapshot(self):
        cmd = """python ../../main.py live delete-live-stream-domain-snapshot  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_live_stream_snapshot_notify_config(self):
        cmd = """python ../../main.py live describe-live-stream-snapshot-notify-config  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_snapshot_notify_config(self):
        cmd = """python ../../main.py live delete-live-stream-snapshot-notify-config  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_forbid_live_stream(self):
        cmd = """python ../../main.py live forbid-live-stream  --app-name 'xxx' --publish-domain 'xxx' --stream-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_resume_live_stream(self):
        cmd = """python ../../main.py live resume-live-stream  --app-name 'xxx' --publish-domain 'xxx' --stream-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_set_live_stream_notify_config(self):
        cmd = """python ../../main.py live set-live-stream-notify-config  --publish-domain 'xxx' --notify-url 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_live_stream_notify_config(self):
        cmd = """python ../../main.py live describe-live-stream-notify-config  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_notify_config(self):
        cmd = """python ../../main.py live delete-live-stream-notify-config  --publish-domain 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_domain_transcode(self):
        cmd = """python ../../main.py live add-live-stream-domain-transcode  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_app_transcode(self):
        cmd = """python ../../main.py live add-live-stream-app-transcode  --publish-domain 'xxx' --template 'xxx' --app-name 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_custom_live_stream_transcode_template(self):
        cmd = """python ../../main.py live add-custom-live-stream-transcode-template  --video-code-rate '5' --video-frame-rate 'xxx' --width '5' --height '5' --template 'xxx' --audio-codec 'xxx' --audio-format 'xxx' --audio-sample-rate '5' --audio-channel '5' --audio-code-rate '5'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_transcodes(self):
        cmd = """python ../../main.py live describe-custom-live-stream-transcodes """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_live_stream_transcode_config(self):
        cmd = """python ../../main.py live describe-live-stream-transcode-config """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_domain_transcode(self):
        cmd = """python ../../main.py live delete-live-stream-domain-transcode  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_app_transcode(self):
        cmd = """python ../../main.py live delete-live-stream-app-transcode  --publish-domain 'xxx' --app-name 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_transcode(self):
        cmd = """python ../../main.py live describe-custom-live-stream-transcode  --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_custom_live_stream_transcode_template(self):
        cmd = """python ../../main.py live delete-custom-live-stream-transcode-template  --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_custom_live_stream_watermark_template(self):
        cmd = """python ../../main.py live add-custom-live-stream-watermark-template  --offset-x '5' --offset-y '5' --width '5' --height '5' --template 'xxx' --url 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_watermark_templates(self):
        cmd = """python ../../main.py live describe-custom-live-stream-watermark-templates """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_app_watermark(self):
        cmd = """python ../../main.py live add-live-stream-app-watermark  --app-name 'xxx' --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_add_live_stream_domain_watermark(self):
        cmd = """python ../../main.py live add-live-stream-domain-watermark  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_describe_custom_live_stream_watermark_config(self):
        cmd = """python ../../main.py live describe-custom-live-stream-watermark-config """
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_custom_live_stream_watermark_template(self):
        cmd = """python ../../main.py live delete-custom-live-stream-watermark-template  --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_app_watermark(self):
        cmd = """python ../../main.py live delete-live-stream-app-watermark  --publish-domain 'xxx' --app-name 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

    def test_delete_live_stream_domain_watermark(self):
        cmd = """python ../../main.py live delete-live-stream-domain-watermark  --publish-domain 'xxx' --template 'xxx'"""
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)

