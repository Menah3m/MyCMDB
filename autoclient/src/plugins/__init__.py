from lib.config.settings import settings
import importlib

class PluginManager(object):
    def __init__(self, hostname=None):
        self.plugin_dict = settings.PLUGIN_DICT
        self.mode = settings.MODE
        self.hostname = hostname
        self.debug = settings.DEBUG
        if self.mode == 'ssh':
            self.user = settings.SSH_USER
            self.pwd = settings.SSH_PWD
            self.port = settings.SSH_PORT
    ### 管理配置文件中采集的插件
    def execute(self):
        
        response  = {}
        # 1.获取配置文件中PLUGIN_DICT  循环获取key和value
        for k, v in self.plugin_dict.items():
            ## k: basic
            ## v: src.plugins.basic.Basic
            module_name, class_name = v.rsplit('.', 1)   
        # 2.将value中的 类 导入并实例化，然后执行process
            ## 如何将一个包以字符串形式导入
            module_path = importlib.import_module(module_name)
            cls = getattr(module_path, class_name)
            res = cls().process(self._cmd_run, self.debug)
            response[k] = res
        return response

    def _cmd_run(self, cmd):
        if self.mode == 'agent':
            return self.__cmd_agent(cmd)   
        elif self.mode =='ssh':            
            return self.__cmd_ssh(cmd)
        elif self.mode == 'salt':
            return self.__cmd_salt(cmd)  
        else:
            raise Exception("当前支持的模式只有：agent/ssh/salt模式")
    
    def __cmd_agent(self, cmd):
        import subprocess
        res = subprocess.getoutput(cmd)
        return res

    def __cmd_ssh(self, cmd):
        import paramiko
        # 创建ssh对象
        ssh = paramiko.SSHClient()
        #允许连接不在know_hosts列表文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接服务器
        ssh.connect(hostname=self.hostname, port=self.port, username=self.user, password=self.pwd)
        #执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        #获取命令结果
        res = stdout.read()
        #关闭连接
        ssh.close
        return res

    def __cmd_salt(self, cmd):
        import subprocess
        res = subprocess.getoutput("salt '%s' cmd.run '%s'"%(self.hostname, cmd))
        return res
