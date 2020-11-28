import unittest
import os
import time
from config_parser  import cconfigparser



class RunMonkey(unittest.TestCase):

    def setUp(self):
        self.config = cconfigparser(r'F:\\python\\monkey_test\\config.ini')
        self.package_name = self.read_config()[2]
        self.clickCount = self.read_config()[1]
        self.execCount = self.read_config()[0]
        self.fpath = self.read_config()[3]
        self.cmd = self.read_config()[4]

    # 获取配置
    def read_config(self):
        config = self.config
        exec_count = config.get('adb', 'execount')
        monkey_clickcout = config.get('adb', 'monkeyClickcount')
        package_name = config.get('adb', 'packageName')
        fpath = config.get('adb', 'fpath')
        cmd = config.get('adb', 'cmd')
        return exec_count, monkey_clickcout, package_name, fpath, cmd

    # 执行monkey
    def runmonkey(self):
        cmd = self.cmd.format(self.package_name.strip('\''), int(self.clickCount), self.fpath.strip('\''))
        result_file = os.popen(cmd.strip('\''), 'r')
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
