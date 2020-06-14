"""
采集服务器的主板信息
Manufacturer：
Product Name：
Serial Number：


"""

import os
from lib.config.settings import settings

class Board(object):

    def process(self, command_func, debug):
        if debug:
            res = open(os.path.join(settings.BASEDIR,'files/board.txt'), 'r', encoding='utf-8').read()
        else:
            res = command_func('sudo dmidecode -t1')
        return self.parse(res)

    def parse(self, res):
        ### 数据筛选
        key_map = {
            'Manufacturer':'manufacturer',
            'Product Name':'product-name',
            'Serial Number':'serial-number',
        }
        res= s.split('\n')
        result = {}

        for info in res:
            if info:
                v = info.strip().split(':')
                if len(v) == 2:
                    if v[0] in key_map:
                        result[key_map[v[0]]]=v[1] 
        return result     