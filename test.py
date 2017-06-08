# 导入tutotial/__init__.py中__all__定义的模块
from tutorial import *

functions.print_info(1,2,3)
''' 模块定义 '''
print('模块basics定义：' + str(dir(basics)))
print('module name: ' + basics.__name__)
print('module package: ' + basics.__package__)
print('module file: ' + basics.__file__)
# print('module builtins: ' + str(basics.__builtins__))
print('module cached: ' + basics.__cached__)
print('module doc:' + str(basics.__doc__))
print('module loader: ' + str(basics.__loader__))
print('module spec: ' + str(basics.__spec__))

print('\n')

''' 类的定义 '''
basic = basics.PythonBasics()
# basic.test_keyword()
print('类PythonBasics定义： '+ str(dir(basic)))
print('class: ' + str(basic.__class__))
print('module: ' + str(basic.__module__))
print('call: ' + str(basic.__call__))
print('dict: ' + str(basic.__dict__))
print('weakref: ' + str(basic.__weakref__))
print('init: ' + str(basic.__init__))


