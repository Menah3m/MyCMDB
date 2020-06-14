# 启动


from lib.config.settings import settings
from src.plugins import PluginManager
from src.plugins import basic, cpu, disk, memory, nic

if __name__ == '__main__':
    

    res = PluginManager().execute()
    print(res)
    # ssh
    # host_list = ['c1.com', 'c2.com']
    # for host in host_list：
    #     res = PluginManager(host).execute()
    #     print(res)

    # basic.Basic().process()
    # cpu.Cpu().process()
    # memory.Memory().process()
    # disk.Disk().process()
    # nic.Nic().process()