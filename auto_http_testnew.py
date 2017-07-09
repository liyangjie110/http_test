# -*- coding: utf_8 -*-
import unittest
import time

from mock import self

from HttpLibrary import HttpApi
import HTMLTestRunner
import sys
import requests
reload(sys)
sys.setdefaultencoding('utf-8')


class TestApi(unittest.TestCase):
    def setUp(self):
        self.api=HttpApi()

    def test_login(self):
        '''测试登录接口'''
        url="http://www.4snow.cn/Home/Index/go/op/login"
        data={'login':'xiaogu','pwd':'123456'}
        results=self.api.http_request("POST",url,data,False)
        self.assertEqual(results['status'],0)
        self.assertEqual(results['data']['username'],u'销顾')

    def test_add_custom(self):
        '''测试添加客户接口'''
        url = "http://www.4snow.cn/Business/Cust/go/op/add"
        data = {'cust[name]': 'ljb' + str(time.time()), 'cust[tel1]': '13800138000'}
        result = self.api.http_request("POST", url, data, True)
        self.assertEqual(result['status'], 0)
        self.assertTrue(str(result).find('id'))

    def test_edit_custom(self):
        '''测试修改客户信息接口'''
        url = "http://www.4snow.cn/Business/Cust/go/op/add"
        data = {'cust[name]': 'ljb' + str(time.time()), 'cust[tel1]': '13800138000'}
        result = self.api.http_request("POST", url, data, True)
        id = result['data']['id']
        url = "http://www.4snow.cn/Business/Cust/go/op/update"
        data = {'cust[id]': id, 'cust[name]': 'ljb' + str(time.time()), 'cust[tel1]': '13800138000'}
        result = self.api.http_request("POST", url, data, True)
        self.assertEqual(result['status'], 0)

    def test_delete_custom(self):
        '''测试删除客户接口'''
        url = "http://www.4snow.cn/Business/Cust/go/op/add"
        data = {'cust[name]': 'ljb' + str(time.time()), 'cust[tel1]': '13800138000'}
        result = self.api.http_request("POST", url, data, True)
        id = result['data']['id']
        url = "http://www.4snow.cn/Business/Cust/go/op/delete"
        data = {'id': id}
        result = self.api.http_request("POST", url, data, True)
        self.assertEqual(result['status'], 0)


def Suite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestApi("test_login"))
    testunit.addTest(TestApi("test_add_custom"))
    testunit.addTest(TestApi("test_edit_custom"))
    testunit.addTest(TestApi("test_delete_custom"))
    return testunit



if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "d:\\result\\" + now + "HTMLtemplate.html"
    print HtmlFile
    fp = file(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"云杉接口测试报告", description=u"用例测试执行情况")
    runner.run(Suite())



