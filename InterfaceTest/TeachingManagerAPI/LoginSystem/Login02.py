import requests
import unittest

#输入正确用户名和空密码，对接口进行错误验证
class MyTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://localhost:/api/mgr/loginReq'
        self.username = 'auto'
        self.password = ''

    def test_login02(self):
        data = {
            'username': self.username,
            'password': self.password
        }
        # 不需要请求头也行
        headers = {
            'Host': 'restapi-teach.com',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(self.url, data=data, headers=headers)
        resValue = response.json()
        resHeaders = response.headers

        print('响应数据信息 %s \n响应请求头信息%s'%(response.json(),response.headers))
        # 1.判断状态码
        self.assertEqual(response.status_code, 200)
        # 2.断言响应数据
        self.assertEqual(resValue['retcode'], 1)
        self.assertEqual(resValue['reason'],'用户或者密码错误')
        # 3.断言响应数据类型
        for key in resHeaders:
            if key == 'Content-Type':
                self.assertEqual(resHeaders[key], "application/json")
            # print(key+":"+resHeaders[key])

    def tearDown(self):
        print("本次接口测试结束！！！")


if __name__=="__mian__":
    unittest.main()
