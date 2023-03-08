# coding=utf-8
from unittest import mock
from collections import Counter

from hn_site_grouper import SiteSourceGrouper as SiteSourceGrouperO


@mock.patch('hn_site_grouper.requests.get')
def test_grouper_returning_valid_type(mocked_get):
    """测试 get_groups 是否返回了正确类型"""
    with open('static_hn.html', 'r', encoding='utf-8') as fp:
        mocked_get.return_value.text = fp.read()

    grouper = SiteSourceGrouperO('https://news.ycombinator.com/')
    result = grouper.get_groups()
    assert isinstance(result, Counter), "groups should be Counter instance"

import unittest
from unittest import mock

from test_modular import Count


# 测试 Count 类
class TestCount(unittest.TestCase):

    # @mock.patch.object(类名，"类中函数名")
    @mock.patch.object(Count, "add")
    def test_add(self, mock_add):
        mock_add.return_value = 13

        result = mock_add()
        self.assertEqual(result, 13)


import unittest
from unittest import mock
import test_modular


class TestLinuxTool(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # @mock.patch(模块名，"函数名")
    @mock.patch("modular.send_shell_cmd")
    def test_check_cmd_response(self, mock_send_shell_cmd):
        mock_send_shell_cmd.return_value = "Response from emulated mock_send_shell_cmd function"

        status = modular.check_cmd_response()
        print("check result: %s" % status)
        self.assertTrue(status)


if __name__ == '__main__':
    unittest.main()
