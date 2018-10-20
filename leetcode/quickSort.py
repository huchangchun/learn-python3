#encoding=utf-8
"""
快速排序：思想是分治法，通过第一个作为分界线，分出比它小的和比它的的数，然后组合起来，小的组里面再细分，大的也在细分
最后组合
如果长度小于2则，输出
否则取数组第一个
小于等于第一个的放less数组中
大于第一个的放greate数组中
递归: fun(less) + [第一个] + fun(greate)
"""
def quickSort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <=pivot]
        greate = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greate)
arr = [1,3,2,5,6,4,5,8]
print(quickSort(arr))