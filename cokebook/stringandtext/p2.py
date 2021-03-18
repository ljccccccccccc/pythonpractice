"""
# 2.2 在字符串开头/结尾做文本匹配
# @Author: ljccccccccccc@163.com Kingorld
# @Date: 2021/3/17 17:11
# @Problem: 在字符串开头/结尾做文本匹配
# @Resolve: str.startswith()  str.endswith() 或者正则表达式 或者切片  但是切片实在不优雅
# @Scene: 检查文件的扩展名，检查url
"""

filename = 'aaa.txt'
res1 = filename.startswith('a')
res2 = filename.endswith('.txt')


url = 'http://www.baidu.com'

res3 = url.startswith('https')
res4 = url.startswith('http')

if __name__ == '__main__':
    print(res1)
    print(res2)
    print('-------------------')
    print(res3)
    print(res4)

