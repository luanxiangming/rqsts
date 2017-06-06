# 导入tutotial/__init__.py中__all__定义的模块
from tutorial import *


functions.print_info(1,2,3)
basic = basics.PythonBasics()
basic.test_type()

print(dir(basics))
print(basics.__name__)
print(basics.__package__)
print(basics.__file__)