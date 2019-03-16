
import os
import logging.config

logger_file_path = r'./log/'
logger_file_name = r'test.log'

"""
日志模块是遵循单列模式，因此实例化多个日志对象的情况下会出现输出信息重复的情况，
这是多个实例化日志记录器使用的是一个
"""


class LoggerTest:

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                                          filename='test.log',
                                          filemode='w',
                                          format="%(asctime)s - "
                                                 "%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter("%(asctime)s - "
                                               "%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
        logging.getLogger('').addHandler(console)
        self.logger = logging

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)


class LoggerLoggert:
    """自动创建日志文件"""

    def __init__(self, filename='./log/logger.log'):

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        logfile = filename
        fh = logging.FileHandler(logfile, mode='w')
        fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter(
            "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)

    def exception(self, msg):
        self.logger.exception(msg)


if __name__ == '__main__':
    logger = LoggerTest()
    logger.info('日志初始化成功')

