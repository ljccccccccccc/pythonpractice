"""
1.1 将序列分解为单独的对象
@Problem: 将含有N个元素的元祖/序列分解成为N个单独的变量
@Resolve: 任何可迭代的对象，都可以通过简单地赋值操作分解为单独的变量
@Author: ljccccccccccc@163.com kingorld
"""

data = ['data', 1, 2, 3, {'a': 'a'}, (1, 2)]

var1, var2, var3, var4, var5, var6 = data

if __name__ == '__main__':
    print(var1)
    print(var2)
    print(var3)
    print(var4)
    print(var5)
    print(var6)
