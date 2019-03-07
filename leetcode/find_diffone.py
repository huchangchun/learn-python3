# -*- coding:utf-8 -*-
class Solution:
    def find_only_one(self, list):
        count = len(list)
        a = None
        for i in range(count):
            if i==0:
                x = list[i]
            else:
                x = x^list[i]
        return x
if __name__=="__main__":
    Test = Solution()
    lst=[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11,11,12,12]
    the_only_one = Test.find_only_one(lst)
    print(the_only_one)