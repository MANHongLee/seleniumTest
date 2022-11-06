import HTMLTestRunner
import time
import os
import unittest


if __name__ == '__main__':
    # 报告名称
    report_name = 'report_{}.html'.format(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
    # 报告路径
    report_url = '/Users/liminkang/Desktop' + os.sep + report_name
    # 查找当前目录下符合的测试用例，构建测试集合
    suite = unittest.defaultTestLoader.discover('.')

    # 通过class构建测试集合（class下面的所有测试用例都会被执行）
    # test_cases = unittest.TestLoader().loadTestsFromTestCase(test_login.TestLogin)
    # suite = unittest.TestSuite([test_cases])

    # 生成测试报告
    with open(report_url, 'wb') as f:
        # 执行测试用例，并生成测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="企业数字化平台-登陆测试报告", description="企业数字化平台-登陆的测试")
        runner.run(suite)
