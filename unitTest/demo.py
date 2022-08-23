
#单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
#unittest中最核心的四部分是：TestCase，TestSuite，TestRunner，TestFixture
# 详解unittest中的基础知识点：断言、测试固件、suite、如何控制用例执行顺序、如何把测试结果输出到文件；
# 详解unittest中的高级知识点：@unittest.skip、@unittest.expectedFailure、failfast、参数化；

import unittest
# from test_mathfunc import TestMathFunc

class TestMathFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual (3, add(1, 2))

    def test_minus(self):
        self.assertEqual (1, minus(3, 2))

    def test_multi(self):
        self.assertEqual (6, multi(3, 2))

    def test_divide(self):
        self.assertEqual (2, divide(6, 2))


if __name__ == '__main__':
    suite = unittest.TestSuite()

    #手动加载指定
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)

    with open('UnittestTextReport.txt', 'a') as  f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)

    #自动搜索方式加载全部
    # ./表示当前目录
    test_dir = './'
    # 找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到文件名时才加载
    # start_dir：要测试的模块名或测试用例目录
    # pattern='test*.py':匹配以“test”开头的.py 类型的文件
    # top_level_dir= None ：测试模块的顶层目录，如果没有顶层目录，默认为None
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    runner = unittest.TextTestRunner()
    runner.run(discover)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(tests)


