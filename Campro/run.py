# encoding=GBK
import os
import time
import unittest
from BeautifulReport import BeautifulReport
from testcase.regwithgg import regwithgg

if __name__ == '__main__':
    '''���Խű�������'''
    Suite = unittest.TestSuite()
    Suite.addTest(unittest.TestLoader().loadTestsFromTestCase(regwithgg))

    list = [Suite]
    suite = unittest.TestSuite(list)

    report_dir = os.path.abspath('.').split('src')[0] + "/report/"
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
    reportFile =  now + "-���Ա���.html"

    BeautifulReport(suite).report(filename=reportFile, description='campro', report_dir=report_dir)

