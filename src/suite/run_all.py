import unittest
from utils import HTMLTestRunner
import time
from utils.mail import Email
from utils.config import REPORT_PATH


def create_test_suite():
    test_list_path = "../testcase"
    test_unit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_list_path, pattern="test_*.py")
    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTest(test_case)
            print(test_case)

    return test_unit

all_test = create_test_suite()
now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

report = REPORT_PATH+'\\'+now_time+'report.html'
with open(report, "wb") as outfile:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title=u"管理端测试报告",
        description=u"用例执行情况：",
        verbosity=2
    )
    runner.run(all_test)
e = Email(path=report, message="详情请下载后打开查看测试报告结果")
e.send()