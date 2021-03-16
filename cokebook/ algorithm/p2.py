"""
# 1.2 从任意长度的可迭代对象中分解元素
# @Author: ljccccccccccc@163.com Kingorld
# @Date: 2021/3/16 16:57
# @Problem: 需要从某个可迭代对象中分解出N个元素，但是这个可迭代对象的长度可能超过N，也就是可能会出现“too many values to unpack”异常
# @Resolve: 使用 *args 解决此问题
# @Scene: 裁判评分需要去掉最高分和最低分，只保留中间的值，然后求平均
"""


def drop_first_last(grades):
    """
    去掉最大值最小值
    """
    first, *middle, last = grades
    return avg(middle)


def avg(*args):
    """
    求平均值
    """
    sum = 0
    for i in args:
        # 遍历第一次取到可变参数的第一个参数 -- (1-9)
        length = len(i)
        for j in i:
            # 循环第二次，真正地遍历数组
            sum += j
        avg = sum/length
        print(avg)
        print("sum = %d" % sum)
        print("length = %d" % length)
        if i is not None:
            return avg
        else :
            return 0


if __name__ == "__main__":
    grades = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    # print(drop_first_last(grades))
    print(avg(grades,1,2,3,4))