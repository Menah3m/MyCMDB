"""
采集服务器的基本信息
hostname：
ip：
mac：


"""


from lib.config.settings import settings

class Basic(object):

    def process(self):

        print("This is Basic Infomation Collector")
        mode = settings.MODE

        if mode == 'agent':
            import subprocess
            res = subprocess.getoutput("ipconfig")
            ip_info = res[205:223]
            print(ip_info)
        elif mode == 'ssh':
            import paramiko
            # 创建SSH对象
            ssh = paramiko.SSHClient()
            # 允许连接不在know_hosts文件中的主机
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务器
            ssh.connect(hostname='', port=22, username=settings.USER, password=settings.PWD)
            # 执行命令
            stdin, stdout, stderr = ssh.exec_command('ipconfig')
            # 获取结果
            res = stdout.read()
            # 关闭连接
            ssh.close()
            ip_info = res[205:223]
            print(ip_info)
        else:
            import subprocess
            res = subprocess.getoutput("salt 'hostname' cmd.run 'ifconfig'")
            ip_info = res[203:224]
            print(ip_info)