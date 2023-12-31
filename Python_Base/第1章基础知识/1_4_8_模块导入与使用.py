# Python默认安装仅包含部分基本或核心模块，但用户可以安装大量的扩展模块，pip是管理模块的重要工具。
# 在Python启动时，仅加载了很少的一部分模块，在需要时由程序员显式地加载（可能需要先安装）其他模块。
# 减小运行的压力，仅加载真正需要的模块和功能，且具有很强的可扩展性。
# 可以使用sys.modules.items()显示所有预加载模块的相关信息。

# import 模块名
import math
print(math.sin(0.5))               #求0.5的正弦
import random
x = random.random( )        #获得[0,1) 内的随机小数
y = random.random( )
n = random.randint(1,100)   #获得[1,100]上的随机整数
print(x,y,n)

# 可以使用dir()函数查看任意模块中所有的对象列表，如果调用不带参数的dir()函数，则返回当前作用域所有名字列表。
# 可以使用help()函数查看任意模块或函数的使用帮助。


# from 模块名 import 对象名[ as 别名] #可以减少查询次数，提高执行速度
# from math import *    #谨慎使用

from math import sin
print(sin(3))
# 0.1411200080598672
from math import sin as f #别名
print(f(3))
# 0.141120008059867


# Python首先在当前目录中查找需要导入的模块文件，如果没有找到则从sys模块的path变量所指定的目录中查找。可以使用sys模块的path变量查看python导入模块时搜索模块的路径，也可以向其中append自定义的目录以扩展搜索路径。
# 在导入模块时，会优先导入相应的pyc文件，如果相应的pyc文件与py文件时间不相符，则导入py文件并重新编译该模块。

# 导入模块时的文件搜索顺序
# 当前文件夹
# sys.path变量指定的文件夹
# 优先导入pyc文件

# 如果需要导入多个模块，一般建议按如下顺序进行导入：
# 标准库
# 成熟的第三方扩展库
# 自己开发的库


# 每个Python脚本在运行时都有一个“__name__”属性。
# 如果脚本作为模块被导入，则其“__name__”属性的值被自动设置为模块名；
# 如果脚本独立运行，则其“__name__”属性值被自动设置为“__main__”。
# 例如，假设文件nametest.py中只包含下面一行代码：
# print(__name__)
# 在IDLE中直接运行该程序时，或者在命令行提示符环境中运行该程序文件时，运行结果如下：
# __main__
# 而将该文件作为模块导入时得到如下执行结果：
# >>> import nametest
# nametest

# 利用“__name__”属性即可控制Python程序的运行方式。例如，编写一个包含大量可被其他程序利用的函数的模块，而不希望该模块可以直接运行，则可以在程序文件中添加以下代码：
# if __name__ == '__main__':
#     print('Please use me as a module.')
# 这样一来，程序直接执行时将会得到提示“Please use me as a module.”，而使用import语句将其作为模块导入后可以使用其中的类、方法、常量或其他成员。

