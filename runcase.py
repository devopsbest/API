import unittest
from testcity import testWeatherApi
from HTMLTestRunner import HTMLTestRunner

testunit = unittest.TestSuite()
testunit.addTest(testWeatherApi("testWeatherApi"))
fp = open('./result.html','wb')
runner = HTMLTestRunner(stream=fp,title="API测试报告",description="测试执行情况")
runner.run(testunit)
fp.close()