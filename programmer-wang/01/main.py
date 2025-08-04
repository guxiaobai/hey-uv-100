import mymath as mm

from mymath import PI

print(id(mm))
print(dir(mm))



# <class 'module'>
print(type(mm))


## 代码从哪里找
from pprint import pprint
import sys

pprint(sys.path)


# 环境变量

PYTHONPATH


# 目录(优先级的目录高于文件)， 这就是所有的package
mymath/__init__.py