# 导入tutotial/__init__.py中__all__定义的模块
from tutorial import *


functions.print_info(1,2,3)
basic = basics.PythonBasics()
basic.test_type()

print(dir(basic))
print('__name__: ' + basics.__name__)
print('__package__: ' + basics.__package__)
print('__file__: ' + basics.__file__)