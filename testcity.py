import unittest

from globals import CASE,host,row_num
from manageapi import testApi

class testWeatherApi(unittest.TestCase):
    def testWeatherApi(self):
        '''测试获取城市天气接口。'''

        for i in range(0, row_num - 1):
            api = testApi(CASE.method[i], host + CASE.url[i], CASE.data[i])
            apicode = api.getCode()
            apijson = api.getJson()
            if apicode == CASE.status[i]:
                print('{}、{}:测试成功。json数据为:{}'.format(i + 1, CASE.name[i], apijson))

            else:
                print('{}、{}:测试失败'.format(i + 1, CASE.name[i]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
