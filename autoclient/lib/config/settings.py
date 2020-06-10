# 配置信息的实现

from conf import setting
from . import global_settings


class Settings():
    def __init__(self):
        # 集成全局配置文件global_settings中的配置
        for key in dir(global_settings):
            if key.isupper():
                setattr(self, key, getattr(global_settings, key))

        # 集成自定义配置文件setting中的配置
        for key in dir(setting):
            if key.isupper():
                setattr(self, key, getattr(setting, key))


settings = Settings()
