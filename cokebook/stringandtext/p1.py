"""
# 2.1 针对任意多的分隔符拆分字符串
# @Author: ljccccccccccc@163.com Kingorld
# @Date: 2021/3/17 15:53
# @Problem: 需要将字符串分割成不同的字段，但是分隔符（包括之间的空格）在整个字符串中并不一致
# @Resolve: 字符串的splite在此略显单薄，应该使用re包下的splite，即re.splite()
# @Scene: 
"""
str = 'asdf fjdk;asdwer, fiusa,asdf   foo'
import re
list = re.split(r'[;,\s]\s*',str)

if __name__ == '__main__':
    print(list)

"""

"""