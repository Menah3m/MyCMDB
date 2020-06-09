from conf import setting
from . import global_settings


class Settings():
    def __init__(self):
        # 集成自定义配置文件setting中的配置
        for key in dir(setting):
            if key.isupper():
                v = getattr(setting, key)
                setattr(self, key, v)

        for key in dir(global_settings):
            if key.isupper():
                v = getattr(global_settings, key)
                setattr(self, key, v)

settings = Settings()