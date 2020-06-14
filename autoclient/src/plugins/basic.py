"""
采集服务器的基本信息
hostname：
ip：
mac：


"""


from lib.config.settings import settings

class Basic(object):

    def process(self, command_func):
        
        res = command_func('hostname')
        self.parse(res)

    def parse(self, res):
        ### 数据筛选
        pass