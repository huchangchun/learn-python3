#encoding=utf-8
def select_sort(arr):
    """
    选择排序 不申请额外内存
    """
    len_ = len(arr)
    for i in range(len_ - 1):
        for j in range(i+1,len_):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j],arr[i]
    return arr
if __name__ == '__main__':
    list = [4,2,5,6,7,9,1,8,3,10]
    print(select_sort(list))