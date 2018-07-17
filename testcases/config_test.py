import unittest
import os


class ConfigTest(unittest.TestCase):

    add_test_profile_cmd = 'python ../main.py configure add --access-key C0EB9718FD006AA6653E368DD37ED812 ' \
                           '--secret-key 2946477B89BB4B8FC0DB9B820F64583D --endpoint 192.168.180.18 ' \
                           '--scheme http --profile test'

    add_default_profile_cmd = 'python ../main.py configure add --access-key A969CF93D901DBEDE6784D85E823611C ' \
        '--secret-key 5E5D773317144763F66315943F1088F6 --endpoint www.jdcloud-api.com --scheme http'

    def _execute(self, cmd):
        with os.popen(cmd) as f:
            content = f.read()
        return content

    def _add_test_profile(self, expect_msg):
        content = self._execute(ConfigTest.add_test_profile_cmd)
        self.assertTrue(expect_msg in content)

    def _delete_profile(self, name, expect_msg):
        cmd = 'python ../main.py configure delete --profile %s' % name
        content = self._execute(cmd)
        self.assertTrue(expect_msg in content)

    def _use_profile(self, name, expect_msg):
        cmd = 'python ../main.py configure use --profile %s' % name
        content = self._execute(cmd)
        self.assertTrue(expect_msg in content)

    def _show_current_profile(self):
        cmd = 'python ../main.py configure show-current'
        content = self._execute(cmd)
        self.assertTrue('192.168.180.18' in content)

    def _show_all_profiles(self):
        cmd = 'python ../main.py configure show-all'
        content = self._execute(cmd)
        self.assertTrue('192.168.180.18' in content)
        self.assertTrue('www.jdcloud-api.com' in content)

    def test_add_default_profile(self):
        self._execute(ConfigTest.add_default_profile_cmd)

    def test_normal_flow(self):
        self._add_test_profile('Configure successfully')
        self._show_current_profile()
        self._show_all_profiles()
        self._use_profile('default', 'Configure successfully')
        self._delete_profile('test', 'Configure successfully')

    def test_add_test_profile_repeatedly(self):
        self._add_test_profile('Configure successfully')
        self._add_test_profile('Profile test has existed')
        self._use_profile('default', 'Configure successfully')
        self._delete_profile('test', 'Configure successfully')

    def test_can_not_delete_current_profile(self):
        self._add_test_profile('Configure successfully')
        self._use_profile('test', 'Configure successfully')
        self._delete_profile('test', 'Can not delete current profile')
        self._use_profile('default', 'Configure successfully')
        self._delete_profile('test', 'Configure successfully')

    def test_use_not_exist_profile(self):
        self._use_profile('xxx', 'Profile xxx do not exist')
