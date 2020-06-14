"""
采集服务器的基本信息
os_platform：
os_version：
hostname：


"""

import os
from lib.config.settings import settings

class Basic(object):

    def process(self, command_func, debug):
        if debug:
            res = {
                'os_platform':'Linux',
                'os_version':'Centos release 7.0\nKernel\r on an \m',
                'hostname':'c2.com',
            }
        else:
            res = {
                'os_platform':command_func("uname").strip(),
                'os_version':command_func("cat /etc/issue").strip().split('\n')[0],
                'hostname':command_func("hostname").strip(),
            }
        return res
       
 