import unittest
import os
import time


class RunMonkey(unittest.TestCase):
    def setUp(self):
        self.packageName = "com.xinghuowx.wx.debug"

    def runmonkey(self):
        packageName = self.packageName
        cmd = 'adb shell monkey -p {} 10>F:\\python\\selenium-python\\python-selenium2\\monkey_test\\monkey_log\\log.txt'.format(packageName)
        result_file = os.popen(cmd, 'r')
        try:
            text = result_file.read()
            return text
        except IOError:
            print('文件错误')
        finally:
            result_file.close()
    

    def test_runMain(self):
        self.runmonkey()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
