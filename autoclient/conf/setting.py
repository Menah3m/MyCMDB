import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 自定义的配置信息
USER = "root"
PWD = 123

MODE = 'ssh' # agent/ssh/salt

SSH_USER = 'root'
SSH_PWD = '123'
SSH_PORT = 22


DEBUG = True


PLUGIN_DICT = {
    'basic': 'src.plugins.basic.Basic',
    'cpu': 'src.plugins.cpu.Cpu',
    'board':'src.Plugins.board.Board',
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.nic.Nic',

}

