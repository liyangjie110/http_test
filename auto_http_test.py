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
        self.api = HttpApi()


    def test_login(self):
        '''测试登录接口'''
        url = "http://www.4snow.cn/Home/Index/go/op/login"
        data = {'login': 'xiaogu', 'pwd': '123456'}
        result = self.api.http_request("GET", url, data, False)
        self.assertEqual(result['status'], 0)
        self.assertEqual(result['data']['username'], u'销顾')

    def test_error_pwd(self):
        url = "http://www.4snow.cn/Home/Index/go/op/login"
        data = {'login': 'xiaogu', 'pwd': '123333456'}
        result = self.api.http_request("GET", url, data, False)
        self.assertEqual(result['status'], 2)



    def test_edit_pwd(self):
        '''测试修改密码接口'''
        url = "http://www.4snow.cn/Home/Index/go/op/updatepwd"
        data = {'password': '123456', 'newpwd': '123456'}
        result = self.api.http_request("POST", url, data, True)
        self.assertEqual(result['status'], 0)


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



    def test_get_unionquery(self):
        '''测试查询车架号接口'''
        url = "http://www.4snow.cn/Business/Newcarwarehouse/go/op/unionquery2"
        data = {'page': '1', 'size': '20', 'shopid': '3', 'wareids[]': '1', 'order': '', 'qkey': 'LVSHJCAC9GE751169',
                'od_et': '1'}
        result = self.api.http_request("POST",url,data,True)
        self.assertEqual(result['status'], 0)
        self.assertEqual(result['data']['list'][0]['vin'],'LVSHJCAC9GE751169')

    def test_error_pwd(self):
        '''测试错误密码'''
        url = "http://www.4snow.cn/Home/Index/go/op/login"
        data = {'login': 'xiaogu', 'pwd': '12345611'}
        results = self.api.http_request("POST", url, data, True)
        self.assertEqual(results['status'], 2)

    def test_find_car(self):
        '''车辆查找'''
        url='http://www.4snow.cn/Business/Newcarwarehouse/go/op/unionquery'
        data= {'page':'1','size':'20','order':'','od_et':'1'}
        results=self.api.http_request("POST",url,data,True)
        self.assertEqual(results['status'],0)

    def test_choose_car(self):
        '''新车选购'''
        url='http://www.4snow.cn/Business/Cart/go/op/carts'
        data={'gts':'1497835470551'}
        result=self.api.http_request('POST',url,data,True)
        self.assertEqual(result['status'],0)

    # def test_shopp_car(self):
    #     '''创建购物车'''
    #     url='http://www.4snow.cn/Business/Cart/go/op/create'
    #     data = {'customer[name]': 'ljb','customer[id]':'48865','customer[sex]':'男', 'customer[Tel]': '110229'}
    #     result=self.api.http_request("POST",url,data,True)
    #     self.assertEqual(result['status'], 0)

    # def test_delete_allCustom(self):
    #     '''测试批量删除'''
    #     url = "http://www.4snow.cn/Business/Cust/go/op/query"
    #     data = {'page': '1', 'size': '1000', 'querykey': 'ljb', 'range': 'personal'}
    #     result = self.api.http_request("POST", url, data, True)
    #     delete_url = "http://www.4snow.cn/Business/Cust/go/op/delete"
    #
    #     for i in range(len(result['data']['list'])):
    #         id = result['data']['list'][i]['id']
    #         delete_data = {'id': id}
    #         re = self.api.http_request("POST", delete_url, delete_data, True)
    #         self.assertEqual(re['status'], 0)


def Suite():
    testunit = unittest.TestSuite()
    testunit.addTest(TestApi("test_login"))
    testunit.addTest(TestApi("test_edit_pwd"))
    testunit.addTest(TestApi("test_add_custom"))
    testunit.addTest(TestApi("test_edit_custom"))
    testunit.addTest(TestApi("test_delete_custom"))
    testunit.addTest(TestApi("test_get_unionquery"))
    testunit.addTest(TestApi("test_error_pwd"))
    testunit.addTest(TestApi("test_find_car"))
    testunit.addTest(TestApi("test_choose_car"))
  #  testunit.addTest(TestApi("test_shopp_car"))
  #  testunit.addTest(TestApi("test_delete_allCustom"))
    return testunit



if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    HtmlFile = "d:\\result\\" + now + "HTMLtemplate.html"
    print HtmlFile
    fp = file(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"云杉接口测试报告", description=u"用例测试执行情况")
    runner.run(Suite())