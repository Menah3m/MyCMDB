"""
采集服务器的Memory信息


"""


from lib.config.settings import settings

class Memory(object):

    def process(self, command_func, debug):
        if debug:
            pass
        else:
            res = command_func('hostname')
            self.parse(res)

    def parse(self, res):
        ### 数据筛选
        pass