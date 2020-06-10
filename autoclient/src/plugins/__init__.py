from lib.config.settings import settings

class PluginManager(object):
    def __init__(self):
        self.plugin_dict = settings.PLUGIN_DICT
    
    ### 管理配置文件中采集的插件
    def execute(self):
        
        # 1.获取配置文件中PLUGIN_DICT  循环获取key和value
        for k, v in self.plugin_dict.items():
            print(k, v)

        # 2.将value中的 类 导入并实例化，然后执行process

