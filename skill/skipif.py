import unittest


class regwithgg(unittest.TestCase):

    sk = 0

    # def setUp(self):
    #     try:
    #         assert regwithgg.sk == 0
    #     except (AssertionError, Exception)as e:
    #         self.skipTest('skiptest:'+str(e))

    # def test_01(self):
    #     try:
    #         assert 1 == 2
    #     except AssertionError:
    #         regwithgg.sk=1
    #         raise

    def test_01(self):
        try:
            assert 1 == 2
        except AssertionError as e:
            self.skipTest(e)
            raise

    # print(sk==0)

    def test_02(self):
        print('???')

    def test_03(self):
        print('???')


if __name__ == '__main__':
    unittest.main()