import importlib

res = importlib.import_module('s4')
cls = getattr(res, 'Person')
cls().getinfo()