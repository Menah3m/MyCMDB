from lib.config.settings import settings
import importlib

class PluginManager(object):
    def __init__(self):
        self.plugin_dict = settings.PLUGIN_DICT
    
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
            res = cls().process()
            response[k] = res
        return response