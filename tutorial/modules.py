import sys
import functions

for i in sys.argv:
	print("运行参数: " + i)

print('Python路径： ' + str(sys.path))

printinfo = functions.print_info #可以把它赋给一个本地的名称：
printinfo(1, 'optional args')

print(functions.__name__) #每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入

print(dir(functions)) #找到模块内定义的所有名称
print(dir()) #如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
