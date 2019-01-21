import unittest
import os
import json
import time


class NcTest(unittest.TestCase):

    def test_describe_all_containers(self):
        self._describe_all_containers()

    def _describe_all_containers(self):
        cmd = 'python ../main.py nc describe-containers --region-id cn-north-1'
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        self.assertIn('totalCount', result)
        self.assertIn('containers', result)
        return result['containers']

    def test_describe_containers_with_filter(self):
        cmd = '''python ../main.py nc describe-containers --region-id cn-north-1 \
            --input-json '{"filters":[{"name":"status", "values":["running"]}]}' '''

        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        self.assertIn('totalCount', result)
        self.assertIn('containers', result)

    def _describe_single_container(self, container_id):
        cmd = 'python ../main.py nc describe-container --region-id cn-north-1 --container-id ' + container_id
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        self.assertIn('container', result)
        return True

    def _create_container_with_json(self):
        cmd = '''python ../main.py nc create-containers --input-json \
            '{
                "maxCount": 1, 
                "regionId": "cn-north-1",
                "containerSpec": 
                {
                    "instanceType": "g.s1.micro", 
                    "az": "cn-north-1b",  
                    "name": "cli-test",
                    "image": "library/httpd",
                    "command": ["/bin/bash"],
                    "tty": true,
                    "rootVolume": 
                    {
                        "category": "cloud", 
                        "cloudDiskSpec": 
                        {
                            "az": "cn-north-1b", 
                            "name": "testaa", 
                            "diskType": "ssd", 
                            "diskSizeGB": 20
                        }
                    }, 
                    "primaryNetworkInterface": 
                    {
                        "networkInterface": 
                        {
                            "subnetId": "subnet-ejs1bir2b2", 
                            "az": "cn-north-1b"
                        }
                    }
                }
            }'
        '''
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        self.assertIn('containerIds', result)
        return result['containerIds'][0]

    def _create_container_with_file_in_absolute_path(self):
        cmd = 'python ../main.py nc create-containers --input-json \
            "file:///Users/oulinbao/projects/cli/testcases/data/create-container.json"'
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        self.assertIn('containerIds', result)
        return result['containerIds'][0]

    def _create_container_with_hybrid_mode(self):
        cmd = '''python ../main.py nc create-containers --region-id cn-north-1 --input-json \
            '{
                "maxCount": 1, 
                "containerSpec": 
                {
                    "instanceType": "g.s1.micro",
                    "az": "cn-north-1b",
                    "name": "cli-test",
                    "image": "library/httpd",
                    "command": ["/bin/bash"],
                    "tty": true,
                    "rootVolume":
                    {
                        "category": "cloud",
                        "cloudDiskSpec":
                        {
                            "az": "cn-north-1b",
                            "name": "testaa",
                            "diskType": "ssd",
                            "diskSizeGB": 20
                        }
                    },
                    "primaryNetworkInterface":
                    {
                        "networkInterface":
                        {
                            "subnetId": "subnet-ejs1bir2b2",
                            "az": "cn-north-1b"
                        }
                    }
                }
            }'
        '''
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        self.assertIn('containerIds', result)
        return result['containerIds'][0]

    def _start_container(self, container_id):
        cmd = 'python ../main.py nc start-container --region-id cn-north-1 --container-id ' + container_id
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        return result['error'] is None

    def _stop_container(self, container_id):
        cmd = 'python ../main.py nc stop-container --region-id cn-north-1 --container-id ' + container_id
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        return result['error'] is None

    def _delete_container(self, container_id):
        cmd = 'python ../main.py nc delete-container --region-id cn-north-1 --container-id ' + container_id
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        self.assertIsInstance(result, dict)
        return result['error'] is None

    def _exec_create(self, container_id):
        cmd = '''python ../main.py nc exec-create --region-id cn-north-1 --container-id %s \
            --input-json '{"command": ["/bin/bash"], "tty": true}' ''' % container_id
        with os.popen(cmd) as f:
            content = f.read()

        print(content)
        result = json.loads(content)
        if isinstance(result, dict) and result['execId']:
            return True

        return False

    def _try(self, count, wait, func, args):
        try_count = count
        result = False
        while try_count > 0:
            print('try_count=', try_count)
            time.sleep(wait)
            result = func(args)
            if result:
                break
            try_count -= 1
        return result

    def test_service_flow_create_by_file(self):
        container_id = self._create_container_with_file_in_absolute_path()
        time.sleep(5)
        self._test_continued_steps(container_id)

    def test_service_flow_create_by_json(self):
        container_id = self._create_container_with_json()
        time.sleep(5)
        self.assertTrue(self._try(10, 5, self._delete_container, container_id))

    def test_service_flow_create_by_hybrid_mode(self):
        container_id = self._create_container_with_hybrid_mode()
        time.sleep(5)
        self.assertTrue(self._try(10, 5, self._delete_container, container_id))

    def _test_continued_steps(self, container_id):
        self.assertTrue(self._describe_single_container(container_id))
        self.assertTrue(self._try(10, 5, self._start_container, container_id))
        # self.assertTrue(self._try(10, 5, self._exec_create, container_id))
        self.assertTrue(self._try(10, 5, self._stop_container, container_id))
        self.assertTrue(self._try(10, 5, self._delete_container, container_id))

    # ##### use to delete all containers #####
    # def test_delete_all_containers(self):
    #     containers = self._describe_all_containers()
    #     if containers is None:
    #         return
    #
    #     for c in containers:
    #         time.sleep(1)
    #         self._delete_container(c['containerId'])
